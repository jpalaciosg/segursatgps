from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime,timedelta
import json
import pytz

from units.models import Unit
from locations.models import Location
from common.device_reader import DeviceReader

from .forms import ReportForm

# Create your views here.
@login_required
def dashboard_view(request):
    return render(request,'reports/dashboard.html')

@login_required
def fleet_status_view(request):
    units = Unit.objects.filter(account=request.user.profile.account)
    for unit in units:
        unit.device.last_gps_odometer = round(unit.device.last_gps_odometer,1)
        unit.device.last_report = datetime.fromtimestamp(unit.device.last_timestamp)
        unit.device.last_report = unit.device.last_report - timedelta(hours=5)
    return render(request,'reports/fleet-status.html',{
        'units':units,
    })

@login_required
def detailed_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Unit.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit = Unit.objects.get(name=data['unit_name'])
            except Exception as e:
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/detailed-report.html',{
                    'units':units,
                    'form':form,
                })  
            locations = Location.objects.filter(
                unit_name=unit.name,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('-id')
            for location in locations:
                dt = datetime.fromtimestamp(location.timestamp)
                dt = dt - timedelta(hours=5)
                location.datetime = dt.strftime("%Y/%m/%d %H:%M:%S")
                # ignicion
                device_reader = DeviceReader(unit.device)
                location.ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                })
            return render(request,'reports/detailed-report.html',{
                'units':units,
                'locations':locations,
            })
        return render(request,'reports/detailed-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'reports/detailed-report.html',{
        'units':units,
    })

@login_required
def travel_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Unit.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit_name = str(data['unit_name'])
                if len(unit_name) == 0:
                    raise Exception('Campo de unidad vacio')
            except Exception as e:
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/travel-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            return render(request,'reports/travel-report.html',{
                'units':units,
                'form':form,
                'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })
                
        return render(request,'reports/travel-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'reports/travel-report.html',{
        'units':units,
    })

@login_required
def stop_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Unit.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit = Unit.objects.get(name=data['unit_name'])
            except Exception as e:
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/stop-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.filter(
                unit_name=unit.name,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('id')
            locations_qs = locations_qs.order_by('timestamp')
            locations = []
            for location_qs in locations_qs:
                locations.append({
                    'latitude':location_qs.latitude,
                    'longitude':location_qs.longitude,
                    'timestamp':location_qs.timestamp,
                    'speed':location_qs.speed,
                    'attributes':json.loads(location_qs.attributes),
                })
            device_reader = DeviceReader(unit.device)
            stop_report = device_reader.get_stop_report(locations)
            return render(request,'reports/stop-report.html',{
                'unit_name':unit.name,
                'stop_report':stop_report,
                'units':units,
                'form':form,
                'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })
                
        return render(request,'reports/stop-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'reports/stop-report.html',{
        'units':units,
    })

@login_required
def event_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Unit.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit = Unit.objects.get(name=data['unit_name'])
            except Exception as e:
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/detailed-report.html',{
                    'units':units,
                    'form':form,
                })  
            locations = Location.objects.filter(
                unit_name=unit.name,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('-id')
            for location in locations:
                dt = datetime.fromtimestamp(location.timestamp)
                dt = dt - timedelta(hours=5)
                location.datetime = dt.strftime("%Y/%m/%d %H:%M:%S")
                # ignicion
                device_reader = DeviceReader({
                    'deviceid':unit.device,
                    'attributes':json.loads(location.attributes),
                })
                location.ignition = device_reader.detect_ignition_event()
            return render(request,'reports/event-report.html',{
                'units':units,
                'locations':locations,
            })
        return render(request,'reports/event-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'reports/event-report.html',{
        'units':units,
    })