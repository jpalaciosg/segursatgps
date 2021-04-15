from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime,timedelta
import json
from pytz import timezone
from geopy.distance import great_circle

from locations.models import Location
from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor

from .forms import ReportForm,SpeedReportForm,MileageReportForm
from units.models import Device

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria

@login_required
def dashboard_view(request):
    units = Device.objects.filter(account=request.user.profile.account)
    now = datetime.now()
    units_not_transmitted = 0
    current_timestamp = int(datetime.timestamp(now))
    units_in_motion = 0
    units_stopped = 0
    for unit in units:
        timeout = current_timestamp - unit.last_timestamp
        if timeout > 86400:
            units_not_transmitted += 1
        if unit.last_speed > 0:
            units_in_motion += 1
        else:
            units_stopped += 1
    units_transmitting = len(units) - units_not_transmitted
    return render(request,'reports/dashboard.html',{
        'units_transmitting': str(units_transmitting),
        'units_not_transmitted': units_not_transmitted,
        'units_in_motion': units_in_motion,
        'units_stopped': units_stopped,
        'panic_alert': 0,
        'battery_alert': 0,
        'speed_alert': 0,
        'other_alert': 0, 
        'now': gmt_conversor.convert_utctolocaltime(now),
    })

@login_required
def fleet_status_view(request):
    units = Device.objects.filter(account=request.user.profile.account)
    now = datetime.now()
    for unit in units:
        try:
            unit.odometer = round(unit.odometer,1)
            unit.last_report = datetime.fromtimestamp(unit.last_timestamp)
            unit.last_report = gmt_conversor.convert_utctolocaltime(unit.last_report)
        except Exception as e:
            print(e)
    return render(request,'reports/fleet-status.html',{
        'units': units,
        'now': gmt_conversor.convert_utctolocaltime(now),
    })

@login_required
def detailed_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit = Device.objects.get(name=data['unit_name'])
            except Exception as e:
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
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
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('id')
            for location in locations:
                dt = datetime.utcfromtimestamp(location.timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                location.datetime = dt
                # ignicion
                device_reader = DeviceReader(unit.uniqueid)
                location.ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                })
            return render(request,'reports/detailed-report.html',{
                'unit_name':unit.name,
                'units':units,
                'locations':locations,
            })
        return render(request,'reports/detailed-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'reports/detailed-report.html',{
        'units':units,
    })

# TRAVEL REPORT
@login_required
def travel_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit = Device.objects.get(name=data['unit_name'])
            except Exception as e:
                print(e)
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                print(e)
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/travel-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.filter(
                unitid=unit.id,
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
                    'address':location_qs.address,
                    'attributes':json.loads(location_qs.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/travel-report.html',{
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            travel_report = device_reader.generate_travel_report(locations)
            return render(request,'reports/travel-report.html',{
                'unit_name':unit.name,
                'travel_report':travel_report,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })      
        return render(request,'reports/travel-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'reports/travel-report.html',{
        'units':units,
    })

# STOP REPORT
@login_required
def stop_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
        if form.is_valid():
            try:
                unit = Device.objects.get(name=data['unit_name'])
            except Exception as e:
                print(e)
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                print(e)
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/stop-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.filter(
                unitid=unit.id,
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
                    'address':location_qs.address,
                    'attributes':json.loads(location_qs.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/stop-report.html',{
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            stop_report = device_reader.generate_stop_report(locations)
            return render(request,'reports/stop-report.html',{
                'unit_name':unit.name,
                'stop_report':stop_report,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })      
        return render(request,'reports/stop-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'reports/stop-report.html',{
        'units':units,
    })

# REPORTE DE VELOCIDAD
@login_required
def speed_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = SpeedReportForm(data)
        if form.is_valid():
            try:
                unit = Device.objects.get(name=data['unit_name'])
            except Exception as e:
                print(e)
                form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                print(e)
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'reports/speed-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.filter(
                unitid=unit.id,
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
                    'address':location_qs.address,
                    'attributes':json.loads(location_qs.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/speed-report.html',{
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            speed_limit = int(data['speed_limit'])
            speed_report = device_reader.generate_speed_report(locations,speed_limit)
            return render(request,'reports/speed-report.html',{
                'unit_name':unit.name,
                'speed_report':speed_report,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })      
        return render(request,'reports/speed-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'reports/speed-report.html',{
        'units':units,
    })


@login_required
def mileage_report_view(request):
    #POST
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = MileageReportForm(data)
        if form.is_valid():
            try:
                initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
                final_timestamp = final_timestamp+86400
            except Exception as e:
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                print(form.errors)
                return render(request,'reports/mileage-report.html',{
                    'units':units,
                    'form':form,
                })
            result = []
            for unit in units:
                locations = Location.objects.filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp
                ).order_by('timestamp')
                distance_sum = 0
                for i in range(len(locations)):
                    if i != 0:
                        if locations[i-1].latitude != 0.0 and locations[i-1].longitude != 0.0:
                            if locations[i].latitude != 0.0 and locations[i].longitude != 0.0:
                                distance = great_circle(
                                    (
                                        locations[i-1].latitude,
                                        locations[i-1].longitude
                                    ),
                                    (
                                        locations[i].latitude,
                                        locations[i].longitude
                                    ),
                                ).km
                                distance_sum += distance
                result.append(
                    {
                        "unit":unit.name,
                        "initial_date":data['initial_date'],
                        "final_date":data['final_date'],
                        "distance":round(distance_sum,2),
                        "odometer":round(unit.odometer,2),
                    }
                )

            return render(request,'reports/mileage-report.html',{
                'units':units,
                'result':result,
                'form':form,
            })
        return render(request,'reports/mileage-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = Device.objects.filter(account=request.user.profile.account)
    form = MileageReportForm()
    return render(request,'reports/mileage-report.html',{
        'units':units,
        'form':form,
    })