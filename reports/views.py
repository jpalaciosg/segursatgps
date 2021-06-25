from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime,timedelta
import json
from pytz import timezone

from locations.models import Location
from geofences.models import Geofence
from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor

from .forms import ReportForm,SpeedReportForm,MileageReportForm,GroupReportForm,GroupSpeedReportForm
from units.models import Device,Group

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
        print(data)
        if form.is_valid():
            try:
                unit = Device.objects.get(name=data['unit_name'])
            except Exception as e:
                form.add_error('unit_name', e)
            #
            try:
                #initial_datetime_str = f"{data['initial_date']} 00:00:00"
                initial_datetime_str = f"{data['initial_datetime']}:00"
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
                #final_datetime_str = f"{data['final_date']} 00:00:00"
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                form.add_error('final_date', e)
            print(initial_timestamp)
            print(final_timestamp)
            if len(form.errors) != 0:
                return render(request,'reports/detailed-report.html',{
                    'units':units,
                    'form':form,
                })
            #locations = Location.objects.filter(  
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('id')
            for location in locations:
                dt = datetime.utcfromtimestamp(location.timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                location.datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                # ignicion
                device_reader = DeviceReader(unit.uniqueid)
                location.ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                })
            return render(request,'reports/detailed-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
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
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/travel-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('timestamp')
            locations_qs = locations_qs.exclude(latitude=0.0,longitude=0.0)
            locations = []
            for location in locations_qs:
                locations.append({
                    'latitude':location.latitude,
                    'longitude':location.longitude,
                    'timestamp':location.timestamp,
                    'speed':location.speed,
                    'address':location.address,
                    'attributes':json.loads(location.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/travel-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            travel_report = device_reader.generate_travel_report(locations)
            return render(request,'reports/travel-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
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

# GROUP TRIP REPORT
@login_required
def group_trip_report_view(request):
    if request.method == 'POST':
        data = request.POST
        groups = Group.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = GroupReportForm(data)
        if form.is_valid():
            try:
                group = Group.objects.get(name=data['group_name'])
            except Exception as e:
                print(e)
                form.add_error('group_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/group-trip-report.html',{
                    'groups':groups,
                    'form':form,
                })
            
            group_trip_report = []
            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp
                ).order_by('timestamp')
                locations_qs = locations_qs.exclude(latitude=0.0,longitude=0.0)
                locations = []
                for location in locations_qs:
                    locations.append({
                        'latitude':location.latitude,
                        'longitude':location.longitude,
                        'timestamp':location.timestamp,
                        'speed':location.speed,
                        'address':location.address,
                        'attributes':json.loads(location.attributes),
                    })
                if len(locations) == 0:
                    return render(request,'reports/group-trip-report.html',{
                        'initial_datetime':data['initial_datetime'],
                        'final_datetime':data['final_datetime'],
                        'groups':groups,
                        'form':form,
                        'error':'No existe un recorrido para analizar.'
                    })
                device_reader = DeviceReader(unit.uniqueid)
                trip_report = device_reader.generate_travel_report(locations)
                for item in trip_report:
                    item['unit_name'] = unit.name 
                    group_trip_report.append(item)
            return render(request,'reports/group-trip-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'group_name':group.name,
                'group_trip_report':group_trip_report,
                'groups':groups,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })

        return render(request,'reports/group-trip-report.html',{
            'groups':groups,
            'form':form,
        })
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-trip-report.html',{
        'groups':groups,
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
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/stop-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('id')
            locations_qs = locations_qs.order_by('timestamp')
            locations = []
            for location in locations_qs:
                locations.append({
                    'latitude':location.latitude,
                    'longitude':location.longitude,
                    'timestamp':location.timestamp,
                    'angle':location.angle,
                    'speed':location.speed,
                    'address':location.address,
                    'attributes':json.loads(location.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/stop-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            stop_report = device_reader.generate_stop_report(locations,initial_timestamp,final_timestamp)
            return render(request,'reports/stop-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
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

# GROUP STOP REPORT
@login_required
def group_stop_report_view(request):
    if request.method == 'POST':
        data = request.POST
        groups = Group.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = GroupReportForm(data)
        if form.is_valid():
            try:
                group = Group.objects.get(name=data['group_name'])
            except Exception as e:
                print(e)
                form.add_error('group_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/group-stop-report.html',{
                    'groups':groups,
                    'form':form,
                })
            
            group_stop_report = []
            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp
                ).order_by('timestamp')
                locations_qs = locations_qs.exclude(latitude=0.0,longitude=0.0)
                locations = []
                for location in locations_qs:
                    locations.append({
                        'latitude':location.latitude,
                        'longitude':location.longitude,
                        'timestamp':location.timestamp,
                        'speed':location.speed,
                        'angle':location.angle,
                        'address':location.address,
                        'attributes':json.loads(location.attributes),
                    })
                if len(locations) == 0:
                    return render(request,'reports/group-stop-report.html',{
                        'initial_datetime':data['initial_datetime'],
                        'final_datetime':data['final_datetime'],
                        'groups':groups,
                        'form':form,
                        'error':'No existe un recorrido para analizar.'
                    })
                device_reader = DeviceReader(unit.uniqueid)
                stop_report = device_reader.generate_stop_report(
                    locations,
                    initial_timestamp,
                    final_timestamp
                )
                for item in stop_report:
                    item['unit_name'] = unit.name 
                    group_stop_report.append(item)
            return render(request,'reports/group-stop-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'group_name':group.name,
                'group_stop_report':group_stop_report,
                'groups':groups,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })

        return render(request,'reports/group-stop-report.html',{
            'groups':groups,
            'form':form,
        })
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-stop-report.html',{
        'groups':groups,
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
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/speed-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.using('history_db_replica').filter(
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
                    'angle':location_qs.angle,
                    'speed':location_qs.speed,
                    'address':location_qs.address,
                    'attributes':json.loads(location_qs.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/speed-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'speed':data['speed'],
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            speed_limit = int(data['speed_limit'])
            speed_report = device_reader.generate_speed_report(locations,speed_limit)
            return render(request,'reports/speed-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'speed_limit':data['speed_limit'],
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

# GROUP SPEED REPORT
@login_required
def group_speed_report_view(request):
    if request.method == 'POST':
        data = request.POST
        groups = Group.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = GroupSpeedReportForm(data)
        if form.is_valid():
            try:
                group = Group.objects.get(name=data['group_name'])
            except Exception as e:
                print(e)
                form.add_error('group_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/group-speed-report.html',{
                    'groups':groups,
                    'form':form,
                })
            
            # Aqui va la logica del resultado
            group_speed_report = []
            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
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
                        'angle':location_qs.angle,
                        'speed':location_qs.speed,
                        'address':location_qs.address,
                        'attributes':json.loads(location_qs.attributes),
                    })
                if len(locations) == 0:
                    return render(request,'reports/group-speed-report.html',{
                        'initial_datetime':data['initial_datetime'],
                        'final_datetime':data['final_datetime'],
                        'groups':groups,
                        'form':form,
                        'error':'No existe un recorrido para analizar.'
                    })
                device_reader = DeviceReader(unit.uniqueid)
                speed_limit = int(data['speed_limit'])
                speed_report = device_reader.generate_speed_report(locations,speed_limit)
                for item in speed_report:
                    item['unit_name'] = unit.name 
                    group_speed_report.append(item)

            return render(request,'reports/group-speed-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'group_name':group.name,
                'group_speed_report':group_speed_report,
                'groups':groups,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })

        return render(request,'reports/group-speed-report.html',{
            'groups':groups,
            'form':form,
        })
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-speed-report.html',{
        'groups':groups,
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
            unit = None
            if data['unit_name'].upper() != 'ALL':
                try:
                    unit = Device.objects.get(name=data['unit_name'])
                except Exception as e:
                    print(e)
                    form.add_error('unit_name', e)
                #
            try:
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                print(form.errors)
                return render(request,'reports/mileage-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'units':units,
                    'form':form,
                })
            result = []
            if data['unit_name'].upper() == 'ALL':
                for unit in units:
                    locations = Location.objects.using('history_db_replica').filter(
                        unitid=unit.id,
                        timestamp__gte=initial_timestamp,
                        timestamp__lte=final_timestamp
                    ).order_by('timestamp')
                    locations = locations.exclude(latitude=0.0,longitude=0.0)
                    device_reader = DeviceReader(unit.uniqueid)
                    distance_sum = device_reader.generate_mileage_report(locations)
                    result.append(
                        {
                            "unit":unit.name,
                            "initial_date":data['initial_datetime'],
                            "final_date":data['final_datetime'],
                            "distance":round(distance_sum,2),
                            "odometer":round(unit.odometer,2),
                        }
                    )
            else:
                locations = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp
                ).order_by('timestamp')
                locations = locations.exclude(latitude=0.0,longitude=0.0)
                device_reader = DeviceReader(unit.uniqueid)
                distance_sum = device_reader.generate_mileage_report(locations)
                result.append(
                    {
                        "unit":unit.name,
                        "initial_date":data['initial_datetime'],
                        "final_date":data['final_datetime'],
                        "distance":round(distance_sum,2),
                        "odometer":round(unit.odometer,2),
                    }
                )
            return render(request,'reports/mileage-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
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

# GROUP MILEAGE REPORT
@login_required
def group_mileage_report_view(request):
    if request.method == 'POST':
        data = request.POST
        groups = Group.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = GroupReportForm(data)
        if form.is_valid():
            try:
                group = Group.objects.get(name=data['group_name'])
            except Exception as e:
                print(e)
                form.add_error('group_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)

            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/group-mileage-report.html',{
                    'groups':groups,
                    'form':form,
                })
            
            # Aqui va la logica del resultado
            group_mileage_report = []
            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp
                ).order_by('id')
                locations_qs = locations_qs.order_by('timestamp')
                locations_qs = locations_qs.exclude(latitude=0.0,longitude=0.0)
                locations = []
                for location_qs in locations_qs:
                    locations.append({
                        'latitude':location_qs.latitude,
                        'longitude':location_qs.longitude,
                        'timestamp':location_qs.timestamp,
                        'angle':location_qs.angle,
                        'speed':location_qs.speed,
                        'address':location_qs.address,
                        'attributes':json.loads(location_qs.attributes),
                    })
                if len(locations) == 0:
                    return render(request,'reports/group-mileage-report.html',{
                        'initial_datetime':data['initial_datetime'],
                        'final_datetime':data['final_datetime'],
                        'groups':groups,
                        'form':form,
                        'error':'No existe un recorrido para analizar.'
                    })
                device_reader = DeviceReader(unit.uniqueid)
                distance_sum = device_reader.generate_mileage_report(locations)
                group_mileage_report.append(
                    {
                        "unit":unit.name,
                        "initial_date":data['initial_datetime'],
                        "final_date":data['final_datetime'],
                        "distance":round(distance_sum,2),
                        "odometer":round(unit.odometer,2),
                    }
                )
            
            return render(request,'reports/group-mileage-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'group_name':group.name,
                'group_mileage_report':group_mileage_report,
                'groups':groups,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })
                

    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-mileage-report.html',{
        'groups':groups,
    })

# GEOFENCE REPORT
@login_required
def geofence_report_view(request):
    #POST
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
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_datetime', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/geofence-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            locations_qs = Location.objects.using('history_db_replica').filter(
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
                    'angle':location_qs.angle,
                    'speed':location_qs.speed,
                    'address':location_qs.address,
                    'attributes':json.loads(location_qs.attributes),
                })
            if len(locations) == 0:
                return render(request,'reports/geofence-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            device_reader = DeviceReader(unit.uniqueid)
            geofences_qs = Geofence.objects.filter(
                account = request.user.profile.account
            )
            geofence_report = device_reader.generate_geofence_report(locations,geofences_qs,initial_timestamp,final_timestamp)
            return render(request,'reports/geofence-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'unit_name':unit.name,
                'geofence_report':geofence_report,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })
        return render(request,'reports/geofence-report.html',{
            'units':units,
            'form':form,
        })

    #GET
    units = Device.objects.filter(account=request.user.profile.account)
    form = ReportForm()
    return render(request,'reports/geofence-report.html',{
        'units':units,
        'form':form,
    })

# GROUP GEOFENCE REPORT
@login_required
def group_geofence_report_view(request):
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-geofence-report.html',{
        'groups':groups,
    })