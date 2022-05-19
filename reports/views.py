from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from datetime import datetime,timedelta
import time
import json
import pandas as pd
from statistics import mean,median
from geopy.distance import great_circle
from shapely.geometry import Point,shape
from common.protocols.time_conversor import TimeConversor

from locations.models import Location
from geofences.models import Geofence
from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

from .forms import ReportForm,StopReportForm,SpeedReportForm,MileageReportForm,GeofenceReportForm,GroupReportForm,GroupSpeedReportForm,GroupStopReportForm,GroupGeofenceReportForm,DetailedMileageReportForm
from .serializers import ReportSerializer,GeofenceReportSerializer
from units.models import Device,Group
from locations.serializers import LocationSerializer

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria
time_conversor = TimeConversor()
privilege = Privilege()

@login_required
def dashboard_view(request):
    units = privilege.get_units(request.user.profile)
    units_transmitting = []
    units_not_transmitted = []
    units_in_motion = []
    units_stopped = []
    now = datetime.now()
    current_timestamp = int(datetime.timestamp(now))

    for unit in units:
        dt = datetime.fromtimestamp(unit.last_timestamp)
        dt = gmt_conversor.convert_utctolocaltime(dt)
        unit.last_report = dt.strftime("%d/%m/%Y %H:%M:%S")
        timeout = current_timestamp - unit.last_timestamp
        if timeout > request.user.profile.account.device_timeout:
            units_not_transmitted.append(unit)
        else:
            units_transmitting.append(unit)
        if unit.last_speed > 0:
            units_in_motion.append(unit)
        else:
            units_stopped.append(unit)
    
    return render(request,'reports/dashboard.html',{
        'units_transmitting': units_transmitting,
        'units_not_transmitted': units_not_transmitted,
        'units_in_motion': units_in_motion,
        'units_stopped': units_stopped,
        'units': units,
        'now': gmt_conversor.convert_utctolocaltime(now),
    })

@login_required
def fleet_status_view(request):
    units = privilege.get_units(request.user.profile)
    now = datetime.now()
    current_timestamp = int(datetime.timestamp(now))
    units_not_transmitted = 0
    units_in_motion = 0
    units_stopped = 0
    for unit in units:
        unit.odometer = round(unit.odometer,1)
        dt = datetime.fromtimestamp(unit.last_timestamp)
        dt = gmt_conversor.convert_utctolocaltime(dt)
        unit.last_report = dt.strftime("%d/%m/%Y %H:%M:%S")
        unit.last_report_date = dt.strftime("%Y/%m/%d %H:%M:%S").split(" ")[0]
        unit.last_report_time = dt.strftime("%Y/%m/%d %H:%M:%S").split(" ")[1]
        ## sumarizar totales
        timeout = current_timestamp - unit.last_timestamp
        if timeout > request.user.profile.account.device_timeout:
            units_not_transmitted += 1
        if unit.last_speed > 0:
            units_in_motion += 1
        else:
            units_stopped += 1
        unit.timeout = int(timeout)
        device_reader = DeviceReader(unit.uniqueid)
        unit.last_ignition = device_reader.detect_ignition_event({
            'attributes':json.loads(unit.last_attributes)
        })
        c_time = device_reader.get_hours({
            'attributes':json.loads(unit.last_attributes)
        })
        hours = int(c_time/3600)
        minutes = int(c_time%3600/60)
        unit.last_hours = f"{hours} h {minutes} m"
        try:
            current_power = json.loads(unit.last_attributes)['power']
        except:
            current_power = 0
        if current_power > 10:
            unit.main_battery = True
            unit.secondary_battery = True
        else:
            unit.main_battery = False
            unit.secondary_battery = True
    units_transmitting = len(units) - units_not_transmitted
    return render(request,'reports/fleet-status.html',{
        'units': units,
        'now': gmt_conversor.convert_utctolocaltime(now),
        'units_transmitting': str(units_transmitting),
        'units_not_transmitted': units_not_transmitted,
        'units_in_motion': units_in_motion,
        'units_stopped': units_stopped,
    })

@api_view(['GET'])
def get_detailed_report(request,unit_name,initial_datetime,final_datetime):
    initial_timestamp = None
    final_timestamp = None
    try:
        unit = Device.objects.get(name=unit_name,account=request.user.profile.account)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    locations = Location.objects.using('history_db_replica').filter(
        unitid=unit.id,
        timestamp__gte=initial_timestamp,
        timestamp__lt=final_timestamp
    ).order_by('timestamp').exclude(
        latitude=0.0,
        longitude=0.0
    )
    serializer = LocationSerializer(locations,many=True)
    device_reader = DeviceReader(unit.uniqueid)
    data = serializer.data
    accumulated_distance = 0.0
    for i in range(len(data)):
        data[i]['unit_name'] = unit.name
        data[i]['unit_description'] = unit.description
        data[i]['attributes'] = json.loads(data[i]['attributes'])
        last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data[i]['timestamp']))
        data[i]['datetime'] = last_report.strftime("%d/%m/%Y %H:%M:%S")
        data[i]['ignition'] = device_reader.detect_ignition_event({
            'attributes':json.loads(locations[i].attributes)
        })
        data[i]['odometer'] = device_reader.get_odometer({
            'attributes':json.loads(locations[i].attributes)
        })
        if i == 0:
            data[i]['distance'] = 0.0
            data[i]['accumulated_distance'] = 0.0
        else:
            distance = great_circle(
                (
                    data[i-1]['latitude'],
                    data[i-1]['longitude']
                ),
                (
                    data[i]['latitude'],
                    data[i]['longitude']
                ),
            ).km
            data[i]['distance'] = round(distance,3)
            accumulated_distance += distance
            data[i]['accumulated_distance'] = round(accumulated_distance,3)

    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def export_detailed_report(request,unit_name,initial_datetime,final_datetime):
    initial_timestamp = None
    final_timestamp = None
    try:
        unit = Device.objects.get(name=unit_name,account=request.user.profile.account)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    locations = Location.objects.using('history_db_replica').filter(
        unitid=unit.id,
        timestamp__gte=initial_timestamp,
        timestamp__lt=final_timestamp
    ).order_by('timestamp').exclude(
        latitude=0.0,
        longitude=0.0
    )
    serializer = LocationSerializer(locations,many=True)
    device_reader = DeviceReader(unit.uniqueid)
    data = serializer.data
    accumulated_distance = 0.0
    for i in range(len(data)):
        data[i]['unit_name'] = unit.name
        data[i]['unit_description'] = unit.description
        data[i]['attributes'] = json.loads(data[i]['attributes'])
        last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data[i]['timestamp']))
        data[i]['datetime'] = last_report.strftime("%d/%m/%Y %H:%M:%S")
        data[i]['ignition'] = device_reader.detect_ignition_event({
            'attributes':json.loads(locations[i].attributes)
        })
        data[i]['odometer'] = device_reader.get_odometer({
            'attributes':json.loads(locations[i].attributes)
        })
        if i == 0:
            data[i]['distance'] = 0.0
            data[i]['accumulated_distance'] = 0.0
        else:
            distance = great_circle(
                (
                    data[i-1]['latitude'],
                    data[i-1]['longitude']
                ),
                (
                    data[i]['latitude'],
                    data[i]['longitude']
                ),
            ).km
            data[i]['distance'] = round(distance,3)
            accumulated_distance += distance
            data[i]['accumulated_distance'] = round(accumulated_distance,3)
    
    path = f'static/tmp/{unit.name}from{initial_datetime.replace(" ","T")}to{final_datetime.replace(" ","T")}.xlsx'
    report = {
        'unit_name': [],
        'unit_description': [],
        'datetime': [],
        'latitude': [],
        'longitude': [],
        'altitude': [],
        'speed': [],
        'distance': [],
        'accumulated_distance': [],
        'odometer': [],
        'ignition': [],
        'address': [],
    }
    for item in data:
        report['unit_name'].append(unit.name) 
        report['unit_description'].append(unit.description)
        report['datetime'].append(item['datetime'])
        report['latitude'].append(item['latitude'])
        report['longitude'].append(item['longitude'])
        report['altitude'].append(item['altitude'])
        report['speed'].append(item['speed'])
        report['distance'].append(item['distance'])
        report['accumulated_distance'].append(item['distance'])
        report['odometer'].append(item['odometer'])
        report['ignition'].append(item['ignition'])
        report['address'].append(item['address'])
    df = pd.DataFrame(report, columns = [
        'unit_name',
        'unit_description',
        'datetime',
        'latitude',
        'longitude',
        'altitude',
        'speed',
        'distance',
        'accumulated_distance',
        'odometer',
        'ignition',
        'address',
    ])
    df.rename(columns={
        'unit_name': 'UNIDAD',
        'unit_description': 'DESCRIPCION',
        'datetime': 'FECHA/HORA',
        'latitude': 'LATITUD',
        'longitude': 'LONGITUD',
        'altitude': 'ALTITUD',
        'speed': 'VELOCIDAD',
        'distance': 'DISTANCIA RECORRIDA',
        'accumulated_distance': 'DISTANCIA ACUMULADA',
        'odometer': 'ODOMETRO',
        'ignition': 'IGNICION',
        'address': 'DIRECCION',
    }, inplace = True)
    df.to_excel (f'templates/{path}', index = False, header=True)

    response = {
        'status': 'OK',
        'path': path,
    }

    return Response(response,status=status.HTTP_200_OK)

@login_required
def detailed_report_view(request):
    # verificar privilegios
    if privilege.view_detailed_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
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

            if len(form.errors) != 0:
                return render(request,'reports/detailed-report.html',{
                    'units':units,
                    'form':form,
                })
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
            if len(locations) == 0:
                return render(request,'reports/detailed-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'units':units,
                    'form':form,
                    'error':'No existe un recorrido para analizar.'
                })
            accumulated_distance = 0.0
            device_reader = DeviceReader(unit.uniqueid)
            for i in range(len(locations)):
                dt = datetime.utcfromtimestamp(locations[i].timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                locations[i].datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                locations[i].ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(locations[i].attributes)
                })
                locations[i].odometer = device_reader.get_odometer({
                    'attributes':json.loads(locations[i].attributes)
                })
                if i == 0:
                    locations[i].distance = 0.0
                    locations[i].accumulated_distance = 0.0
                else:
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
                    locations[i].distance = round(distance,3)
                    accumulated_distance += distance
                    locations[i].accumulated_distance = round(accumulated_distance,3)
            return render(request,'reports/detailed-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'units':units,
                'locations':locations,
            })
        return render(request,'reports/detailed-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/detailed-report.html',{
        'units':units,
    })

@login_required
def detailed_mileage_report_view(request):
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
        initial_timestamp = None
        final_timestamp = None
        form = DetailedMileageReportForm(data)
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

            try:
                mileage = float(data['mileage'])
            except Exception as e:
                form.add_error('mileage', e)

            if len(form.errors) != 0:
                return render(request,'reports/detailed-mileage-report.html',{
                    'units':units,
                    'form':form,
                })
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
            accumulated_distance = mileage
            for i in range(len(locations)):
                dt = datetime.utcfromtimestamp(locations[i].timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                locations[i].datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                # ignicion
                device_reader = DeviceReader(unit.uniqueid)
                locations[i].ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(locations[i].attributes)
                })
                if i == 0:
                    locations[i].distance = 0.0
                    locations[i].accumulated_distance = float(data['mileage'])
                else:
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
                    locations[i].distance = round(distance,3)
                    accumulated_distance += distance
                    locations[i].accumulated_distance = round(accumulated_distance,3)
            return render(request,'reports/detailed-mileage-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'units':units,
                'locations':locations,
            })
        return render(request,'reports/detailed-mileage-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/detailed-mileage-report.html',{
        'units':units,
    })

@login_required
def detailed_report_with_attributes_view(request):
    # verificar privilegios
    if privilege.view_detailed_report_with_attributes(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
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

            if len(form.errors) != 0:
                return render(request,'reports/detailed-report-with-attributes.html',{
                    'units':units,
                    'form':form,
                })
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
            accumulated_distance = 0.0
            for i in range(len(locations)):
                dt = datetime.utcfromtimestamp(locations[i].timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                locations[i].datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                # ignicion
                device_reader = DeviceReader(unit.uniqueid)
                locations[i].ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(locations[i].attributes)
                })
                if i == 0:
                    locations[i].distance = 0.0
                    locations[i].accumulated_distance = 0.0
                else:
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
                    locations[i].distance = round(distance,2)
                    accumulated_distance += distance
                    locations[i].accumulated_distance = round(accumulated_distance,2)
            return render(request,'reports/detailed-report-with-attributes.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'units':units,
                'locations':locations,
            })
        return render(request,'reports/detailed-report-with-attributes.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/detailed-report-with-attributes.html',{
        'units':units,
    })

@api_view(['GET'])
def get_driving_style_report(request,unit_name,initial_datetime,final_datetime):
    initial_timestamp = None
    final_timestamp = None
    unit = None
    if unit_name.upper() != 'ALL':
        try:
            unit = Device.objects.get(
                name=unit_name,
                #account=request.user.profile.account
            )
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    
    locations = Location.objects.using('history_db_replica').filter(
        unitid=unit.id,
        timestamp__gte=initial_timestamp,
        timestamp__lt=final_timestamp
    ).order_by('timestamp').exclude(
        latitude=0.0,
        longitude=0.0
    )
    serializer = LocationSerializer(locations,many=True)
    data = serializer.data

    harsh_driving_report = []
    harsh_braking = 0
    harsh_acceleration = 0
    harsh_cornering = 0
    device_reader = DeviceReader(unit.uniqueid)
    for i in range(len(data)):
        data[i]['unit_name'] = unit.name
        data[i]['unit_description'] = unit.description
        dt = datetime.utcfromtimestamp(data[i]['timestamp'])
        dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
        data[i]['datetime'] = dt.strftime("%d/%m/%Y %H:%M:%S")
        data[i]['ignition'] = device_reader.detect_ignition_event({
            'attributes':json.loads(data[i]['attributes'])
        })
        try:
            driving_incident = json.loads(data[i]['attributes'])['alarm']
            data[i]['driving'] = driving_incident
            data[i]['intensity'] = json.loads(data[i]['attributes'])['io254']
            if driving_incident == 'hardBraking': harsh_braking += 1
            if driving_incident == 'hardAcceleration': harsh_acceleration += 1
            if driving_incident == 'hardCornering': harsh_cornering += 1
            harsh_driving_report.append(data[i])
        except Exception as e:
            pass
    summarization = [
        {
        'unit_name': unit.name,
        'unit_description': unit.description,
        'initial_datetime':initial_datetime,
        'final_datetime':final_datetime,
        'type': 'harshAcceleration',
        'amount': harsh_acceleration
        },
        {
        'unit_name': unit.name,
        'unit_description': unit.description,
        'initial_datetime':initial_datetime,
        'final_datetime':final_datetime,
        'type': 'harshBraking',
        'amount': harsh_braking
        },
        {
        'unit_name': unit.name,
        'unit_description': unit.description,
        'initial_datetime':initial_datetime,
        'final_datetime':final_datetime,
        'type': 'harshCornering',
        'amount': harsh_cornering
        },
    ]
    final_report = {
        'harsh_driving_report':harsh_driving_report,
        'summarization':summarization,
    }    
    return Response(final_report,status=status.HTTP_200_OK)

def driving_style_report_view(request):
    # verificar privilegios
    if privilege.view_driving_style_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
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

            if len(form.errors) != 0:
                return render(request,'reports/driving-style-report.html',{
                    'units':units,
                    'form':form,
                })
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
            harsh_driving_report = []
            for i in range(len(locations)):
                dt = datetime.utcfromtimestamp(locations[i].timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                locations[i].datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                try:
                    locations[i].driving = json.loads(locations[i].attributes)['alarm']
                    locations[i].intensity = json.loads(locations[i].attributes)['io254']
                    harsh_driving_report.append(locations[i])
                except Exception as e:
                    print(e)
            return render(request,'reports/driving-style-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'units':units,
                'locations':harsh_driving_report,
            })
        return render(request,'reports/driving-style-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/driving-style-report.html',{
        'units':units,
    })

@api_view(['GET'])
def get_trip_report1(request,unit_name,initial_datetime,final_datetime,geofence_option):
    initial_timestamp = None
    final_timestamp = None
    unit = None
    if unit_name.upper() != 'ALL':
        try:
            unit = Device.objects.get(
                name=unit_name,
                account=request.user.profile.account
            )
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
        # validar geofence option
        geofence_option = bool(geofence_option)
        # --
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    
    trip_report = []
    summarization = []
    
    if unit_name.upper() == 'ALL':
        units = privilege.get_units(request.user.profile)
        for unit in units:
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
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
            device_reader = DeviceReader(unit.uniqueid)
            unit_trip_report = device_reader.generate_trip_report(locations)
            for item in unit_trip_report:
                item['unit_name'] = unit.name
                item['unit_description'] = unit.description
                trip_report.append(item)

            total_stop_duration = 0
            number_of_trips = 0
            distance = 0.0
            duration = 0

            for tr in unit_trip_report:
                number_of_trips += 1
                distance += tr['distance']
                duration += tr['duration']
                qs = locations_qs.filter(
                    timestamp__gte=tr['initial_timestamp'],
                    timestamp__lte=tr['final_timestamp']
                )
                locations = []
                for item in qs:
                    locations.append({
                        'latitude':item.latitude,
                        'longitude':item.longitude,
                        'timestamp':item.timestamp,
                        'angle':item.angle,
                        'speed':item.speed,
                        'address':item.address,
                        'attributes':json.loads(item.attributes),
                    })
                stop_report = device_reader.generate_stop_report(
                    locations,
                    tr['initial_timestamp'],
                    tr['final_timestamp'],
                    0
                )
                stop_duration = 0
                for sr in stop_report:
                    stop_duration += sr['duration']
                tr['stopped_time'] = str(timedelta(seconds=stop_duration))
                total_stop_duration += stop_duration
                tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))
            
            if len(unit_trip_report) != 0:
                driving_duration = duration - total_stop_duration
                summarization.append({
                    "unit_name" : unit.name,
                    "unit_description": unit.description,
                    "initial_datetime": initial_datetime,
                    "final_datetime" : final_datetime,
                    "number_of_trips": number_of_trips,
                    "distance": round(distance,2),
                    "duration": duration,
                    "time": str(timedelta(seconds=duration)),
                    "driving_time_in_trip": str(timedelta(seconds=driving_duration)),
                    "stopped_time_in_trip": str(timedelta(seconds=total_stop_duration))
                })            

    else:
        locations_qs = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lte=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
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

        device_reader = DeviceReader(unit.uniqueid)
        unit_trip_report = device_reader.generate_trip_report(locations)
        for item in unit_trip_report:
            item['unit_name'] = unit.name
            item['unit_description'] = unit.description
            trip_report.append(item)

        total_stop_duration = 0
        number_of_trips = 0
        distance = 0.0
        duration = 0
        
        for tr in trip_report:
            number_of_trips += 1
            distance += tr['distance']
            duration += tr['duration']
            qs = locations_qs.filter(
                timestamp__gte=tr['initial_timestamp'],
                timestamp__lte=tr['final_timestamp']
            )
            locations = []
            for item in qs:
                locations.append({
                    'latitude':item.latitude,
                    'longitude':item.longitude,
                    'timestamp':item.timestamp,
                    'angle':item.angle,
                    'speed':item.speed,
                    'address':item.address,
                    'attributes':json.loads(item.attributes),
                })
            stop_report = device_reader.generate_stop_report(
                locations,
                tr['initial_timestamp'],
                tr['final_timestamp'],
                0
            )
            stop_duration = 0
            for sr in stop_report:
                stop_duration += sr['duration']
            tr['stopped_time'] = str(timedelta(seconds=stop_duration))
            total_stop_duration += stop_duration
            tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))

        if len(unit_trip_report) != 0:
            driving_duration = duration - total_stop_duration
            summarization.append({
                "unit_name" : unit.name,
                "unit_description": unit.description,
                "initial_datetime": initial_datetime,
                "final_datetime" : final_datetime,
                "number_of_trips": number_of_trips,
                "distance": round(distance,2),
                "duration": duration,
                "time": str(timedelta(seconds=duration)),
                "driving_time_in_trip": str(timedelta(seconds=driving_duration)),
                "stopped_time_in_trip": str(timedelta(seconds=total_stop_duration))
            })
    
    # CALCULAR GEOCERCAS
    if geofence_option:
        geofences = Geofence.objects.filter(account=request.user.profile.account)
        for tr in trip_report:
            matching_initial_geofences = []
            matching_final_geofences = []
            for geofence in geofences:
                feature = json.loads(geofence.geojson)['features'][0]
                s = shape(feature['geometry'])
                point = Point(tr['initial_longitude'],tr['initial_latitude'])
                if s.contains(point):
                    matching_initial_geofences.append(geofence.name)
                point = Point(tr['final_longitude'],tr['final_latitude'])
                if s.contains(point):
                    matching_final_geofences.append(geofence.name)
            s_str = ""
            for i in range(len(matching_initial_geofences)):
                if i==0:
                    s_str += matching_initial_geofences[i]
                else:
                    s_str += f', {matching_initial_geofences[i]}'
            tr['initial_geofences'] = s_str
            d_str = ""
            for i in range(len(matching_final_geofences)):
                if i==0:
                    d_str += matching_final_geofences[i]
                else:
                    d_str += f', {matching_final_geofences[i]}'
            tr['final_geofences'] = d_str
    else:
        for tr in trip_report:
            tr['initial_geofences'] = 'N/D'
            tr['final_geofences'] = 'N/D'
    # FIN - CALCULAR GEOCERCAS

    data = {
        'trip_report': trip_report,
        'summarization': summarization
    }

    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_trip_report2(request,unit_name,initial_datetime,final_datetime,geofence_option):
    unit = None
    if unit_name.upper() != 'ALL':
        try:
            unit = Device.objects.get(name=unit_name,account=request.user.profile.account)
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # validar geofence option
        geofence_option = bool(geofence_option)
        # --
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Aqui va la logica del resultado
    trip_report = []
    summarization = []

    if unit_name.upper() == 'ALL':
        units = privilege.get_units(request.user.profile)
        for unit in units:
            initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
            initial_datetime_obj = initial_datetime_obj.replace(hour=0,minute=0,second=0)
            final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
            datetime_ranges = []
            while initial_datetime_obj < final_datetime_obj:
                datetime_ranges.append([
                    initial_datetime_obj,
                    initial_datetime_obj+timedelta(days=1)
                ])
                initial_datetime_obj = initial_datetime_obj+timedelta(days=1)
            datetime_ranges[0][0] = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
            datetime_ranges[len(datetime_ranges)-1][1] = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
            for dr in datetime_ranges:
                timestamp1 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[0])))
                timestamp2 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[1])))
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=timestamp1,
                    timestamp__lt=timestamp2
                ).order_by('timestamp')
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
                device_reader = DeviceReader(unit.uniqueid)
                unit_trip_report = device_reader.generate_trip_report(locations)

                total_stop_duration = 0
                number_of_trips = 0
                distance = 0.0
                duration = 0

                for tr in unit_trip_report:
                    tr['unit_name'] = unit.name
                    tr['unit_description'] = unit.description
                    number_of_trips += 1
                    distance += tr['distance']
                    duration += tr['duration']
                    qs = locations_qs.filter(
                        timestamp__gte=tr['initial_timestamp'],
                        timestamp__lt=tr['final_timestamp']
                    )
                    locations = []
                    for item in qs:
                        locations.append({
                            'latitude':item.latitude,
                            'longitude':item.longitude,
                            'timestamp':item.timestamp,
                            'angle':item.angle,
                            'speed':item.speed,
                            'address':item.address,
                            'attributes':json.loads(item.attributes),
                        })
                    stop_report = device_reader.generate_stop_report(
                        locations,
                        tr['initial_timestamp'],
                        tr['final_timestamp'],
                        0
                    )
                    stop_duration = 0
                    for sr in stop_report:
                        stop_duration += sr['duration']
                    tr['stopped_time'] = str(timedelta(seconds=stop_duration))
                    total_stop_duration += stop_duration
                    tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))
                    trip_report.append(tr)
                
                if len(unit_trip_report) != 0:
                    driving_duration = duration - total_stop_duration
                    summarization.append({
                        "unit_name" : unit.name,
                        "unit_description": unit.description,
                        "initial_datetime": dr[0].strftime("%Y-%m-%d, %H:%M:%S"),
                        "final_datetime" : dr[1].strftime("%Y-%m-%d, %H:%M:%S"),
                        "number_of_trips": number_of_trips,
                        "distance": round(distance,2),
                        "duration": duration,
                        "time": str(timedelta(seconds=duration)),
                        "driving_time_in_trip": str(timedelta(seconds=driving_duration)),
                        "stopped_time_in_trip": str(timedelta(seconds=total_stop_duration)),
                        "stopped_time": str(timedelta(seconds=(86400-duration))),
                        "percentage_driving_time_in_trip": str(round(driving_duration*100/86400,2))+' %',
                        "percentage_stopped_time_in_trip": str(round(total_stop_duration*100/86400,2))+' %',
                        "percentage_stopped_time": str(round((86400-duration)*100/86400,2))+' %',
                    })     
    else:
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        initial_datetime_obj = initial_datetime_obj.replace(hour=0,minute=0,second=0)
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        datetime_ranges = []
        while initial_datetime_obj < final_datetime_obj:
            datetime_ranges.append([
                initial_datetime_obj,
                initial_datetime_obj+timedelta(days=1)
            ])
            initial_datetime_obj = initial_datetime_obj+timedelta(days=1)
        datetime_ranges[0][0] = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        datetime_ranges[len(datetime_ranges)-1][1] = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        for dr in datetime_ranges:
            timestamp1 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[0])))
            timestamp2 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[1])))
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=timestamp1,
                timestamp__lt=timestamp2
            ).order_by('timestamp')
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
            device_reader = DeviceReader(unit.uniqueid)
            unit_trip_report = device_reader.generate_trip_report(locations)
           
            total_stop_duration = 0
            number_of_trips = 0
            distance = 0.0
            duration = 0

            for tr in unit_trip_report:
                tr['unit_name'] = unit.name
                tr['unit_description'] = unit.description
                number_of_trips += 1
                distance += tr['distance']
                duration += tr['duration']
                qs = locations_qs.filter(
                    timestamp__gte=tr['initial_timestamp'],
                    timestamp__lt=tr['final_timestamp']
                )
                locations = []
                for item in qs:
                    locations.append({
                        'latitude':item.latitude,
                        'longitude':item.longitude,
                        'timestamp':item.timestamp,
                        'angle':item.angle,
                        'speed':item.speed,
                        'address':item.address,
                        'attributes':json.loads(item.attributes),
                    })
                stop_report = device_reader.generate_stop_report(
                    locations,
                    tr['initial_timestamp'],
                    tr['final_timestamp'],
                    0
                )
                stop_duration = 0
                for sr in stop_report:
                    stop_duration += sr['duration']
                tr['stopped_time'] = str(timedelta(seconds=stop_duration))
                total_stop_duration += stop_duration
                tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))
                trip_report.append(tr)

            driving_duration = duration - total_stop_duration
            summarization.append({
                "unit_name" : unit.name,
                "unit_description": unit.description,
                "initial_datetime": dr[0].strftime("%Y-%m-%d, %H:%M:%S"),
                "final_datetime" : dr[1].strftime("%Y-%m-%d, %H:%M:%S"),
                "number_of_trips": number_of_trips,
                "distance": round(distance,2),
                "duration": duration,
                "time": str(timedelta(seconds=duration)),
                "driving_time_in_trip": str(timedelta(seconds=driving_duration)),
                "stopped_time_in_trip": str(timedelta(seconds=total_stop_duration)),
                "stopped_time": str(timedelta(seconds=(86400-duration))),
                "percentage_driving_time_in_trip": str(round(driving_duration*100/86400,2))+' %',
                "percentage_stopped_time_in_trip": str(round(total_stop_duration*100/86400,2))+' %',
                "percentage_stopped_time": str(round((86400-duration)*100/86400,2))+' %',
            })

    # CALCULAR GEOCERCAS
    if geofence_option:
        geofences = Geofence.objects.filter(account=request.user.profile.account)
        for tr in trip_report:
            matching_initial_geofences = []
            matching_final_geofences = []
            for geofence in geofences:
                feature = json.loads(geofence.geojson)['features'][0]
                s = shape(feature['geometry'])
                point = Point(tr['initial_longitude'],tr['initial_latitude'])
                if s.contains(point):
                    matching_initial_geofences.append(geofence.name)
                point = Point(tr['final_longitude'],tr['final_latitude'])
                if s.contains(point):
                    matching_final_geofences.append(geofence.name)
            s_str = ""
            for i in range(len(matching_initial_geofences)):
                if i==0:
                    s_str += matching_initial_geofences[i]
                else:
                    s_str += f', {matching_initial_geofences[i]}'
            tr['initial_geofences'] = s_str
            d_str = ""
            for i in range(len(matching_final_geofences)):
                if i==0:
                    d_str += matching_final_geofences[i]
                else:
                    d_str += f', {matching_final_geofences[i]}'
            tr['final_geofences'] = d_str
    else:
        for tr in trip_report:
            tr['initial_geofences'] = 'N/D'
            tr['final_geofences'] = 'N/D'
    # FIN - CALCULAR GEOCERCAS

    data = {
        'trip_report': trip_report,
        'summarization': summarization
    }
    return Response(data,status=status.HTTP_200_OK)

# TRIP REPORT
@login_required
def trip_report_view(request):
    # verificar privilegios
    if privilege.view_trip_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
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
                print(e)
                form.add_error('final_datetime', e)

            if len(form.errors) != 0:
                return render(request,'reports/trip-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            trip_report = []
            summarization = []
            if data['unit_name'].upper() == 'ALL':
                for unit in units:
                    locations_qs = Location.objects.using('history_db_replica').filter(
                        unitid=unit.id,
                        timestamp__gte=initial_timestamp,
                        timestamp__lt=final_timestamp
                    ).order_by('timestamp')
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
                    device_reader = DeviceReader(unit.uniqueid)
                    unit_trip_report = None
                    try:
                        unit_trip_report = device_reader.generate_trip_report(locations)
                    except Exception as e:
                        unit_trip_report = []
                        print(e)

                    for item in unit_trip_report:
                        item['unit_name'] = unit.name
                        item['unit_description'] = unit.description
                        trip_report.append(item)

                    total_stop_duration = 0
                    number_of_trips = 0
                    distance = 0.0
                    duration = 0 

                    for tr in unit_trip_report:
                        number_of_trips += 1
                        distance += tr['distance']
                        duration += tr['duration']
                        qs = locations_qs.filter(
                            timestamp__gte=tr['initial_timestamp'],
                            timestamp__lt=tr['final_timestamp']
                        )
                        locations = []
                        for item in qs:
                            locations.append({
                                'latitude':item.latitude,
                                'longitude':item.longitude,
                                'timestamp':item.timestamp,
                                'angle':item.angle,
                                'speed':item.speed,
                                'address':item.address,
                                'attributes':json.loads(item.attributes),
                            })
                        stop_report = device_reader.generate_stop_report(
                            locations,
                            tr['initial_timestamp'],
                            tr['final_timestamp'],
                            0
                        )
                        stop_duration = 0
                        for sr in stop_report:
                            stop_duration += sr['duration']
                        tr['stopped_time'] = str(timedelta(seconds=stop_duration))
                        total_stop_duration += stop_duration
                        tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))
                    
                    if len(unit_trip_report) != 0:
                        driving_duration = duration - total_stop_duration
                        summarization.append({
                            "unit_name" : unit.name,
                            "unit_description": unit.description,
                            "number_of_trips": number_of_trips,
                            "distance": distance,
                            "duration": duration,
                            "time": str(timedelta(seconds=duration)),
                            "driving_time": str(timedelta(seconds=driving_duration)),
                            "stopped_time": str(timedelta(seconds=total_stop_duration))
                        })

            else:
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('timestamp')
                locations_qs = locations_qs.exclude(latitude=0.0,longitude=0.0)
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
                    return render(request,'reports/trip-report.html',{
                        'initial_datetime':data['initial_datetime'],
                        'final_datetime':data['final_datetime'],
                        'units':units,
                        'form':form,
                        'error':'No existe un recorrido para analizar.'
                    })

                device_reader = DeviceReader(unit.uniqueid)
                unit_trip_report = None
                try:
                    unit_trip_report = device_reader.generate_trip_report(locations)
                except Exception as e:
                    unit_trip_report = []
                    print(e)

                for item in unit_trip_report:
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    trip_report.append(item)

                total_stop_duration = 0
                number_of_trips = 0
                distance = 0.0
                duration = 0

                for tr in trip_report:
                    number_of_trips += 1
                    distance += tr['distance']
                    duration += tr['duration']
                    qs = locations_qs.filter(
                        timestamp__gte=tr['initial_timestamp'],
                        timestamp__lt=tr['final_timestamp']
                    )
                    locations = []
                    for item in qs:
                        locations.append({
                            'latitude':item.latitude,
                            'longitude':item.longitude,
                            'timestamp':item.timestamp,
                            'angle':item.angle,
                            'speed':item.speed,
                            'address':item.address,
                            'attributes':json.loads(item.attributes),
                        })
                    stop_report = device_reader.generate_stop_report(
                        locations,
                        tr['initial_timestamp'],
                        tr['final_timestamp'],
                        0
                    )
                    stop_duration = 0
                    for sr in stop_report:
                        stop_duration += sr['duration']
                    tr['stopped_time'] = str(timedelta(seconds=stop_duration))
                    total_stop_duration += stop_duration
                    tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))
                
                driving_duration = duration - total_stop_duration
                summarization.append({
                    "unit_name" : unit.name,
                    "unit_description": unit.description,
                    "number_of_trips": number_of_trips,
                    "distance": distance,
                    "duration": duration,
                    #"time": str(timedelta(seconds=duration)),
                    "time": time_conversor.convert_seconds_in_hour_format(duration),
                    #"driving_time": str(timedelta(seconds=driving_duration)),
                    "driving_time": time_conversor.convert_seconds_in_hour_format(driving_duration),
                    #"stopped_time": str(timedelta(seconds=total_stop_duration))
                    "stopped_time": time_conversor.convert_seconds_in_hour_format(total_stop_duration),
                })
            # CALCULAR GEOCERCAS
            geofences = Geofence.objects.filter(account=request.user.profile.account)
            for tr in trip_report:
                matching_initial_geofences = []
                matching_final_geofences = []
                for geofence in geofences:
                    feature = json.loads(geofence.geojson)['features'][0]
                    s = shape(feature['geometry'])
                    point = Point(tr['initial_longitude'],tr['initial_latitude'])
                    if s.contains(point):
                        matching_initial_geofences.append(geofence.name)
                    point = Point(tr['final_longitude'],tr['final_latitude'])
                    if s.contains(point):
                        matching_final_geofences.append(geofence.name)
                s_str = ""
                for i in range(len(matching_initial_geofences)):
                    if i==0:
                        s_str += matching_initial_geofences[i]
                    else:
                        s_str += f', {matching_initial_geofences[i]}'
                tr['initial_geofences'] = s_str
                d_str = ""
                for i in range(len(matching_final_geofences)):
                    if i==0:
                        d_str += matching_final_geofences[i]
                    else:
                        d_str += f', {matching_final_geofences[i]}'
                tr['final_geofences'] = d_str
            # FIN - CALCULAR GEOCERCAS
            return render(request,'reports/trip-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'trip_report':trip_report,
                'summarization':summarization,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
                })      
        return render(request,'reports/trip-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/trip-report.html',{
        'units':units,
    })

# TRIP REPORT
@login_required
def trip_report2_view(request):
    # verificar privilegios
    if privilege.view_trip_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/trip-report2.html',{
        'units':units,
    })

# GROUP TRIP REPORT
@login_required
def group_trip_report_view(request):
    # verificar privilegios
    if privilege.view_group_trip_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
            summarization = []

            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('timestamp').exclude(latitude=0.0,longitude=0.0)
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
                device_reader = DeviceReader(unit.uniqueid)
                unit_trip_report = device_reader.generate_trip_report(locations)
                for item in unit_trip_report:
                    item['group_name'] = group.name
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    group_trip_report.append(item)

                total_stop_duration = 0
                number_of_trips = 0
                distance = 0.0
                duration = 0 

                for tr in unit_trip_report:
                    number_of_trips += 1
                    distance += tr['distance']
                    duration += tr['duration']
                    qs = locations_qs.filter(
                        timestamp__gte=tr['initial_timestamp'],
                        timestamp__lt=tr['final_timestamp']
                    )
                    locations = []
                    for item in qs:
                        locations.append({
                            'latitude':item.latitude,
                            'longitude':item.longitude,
                            'timestamp':item.timestamp,
                            'angle':item.angle,
                            'speed':item.speed,
                            'address':item.address,
                            'attributes':json.loads(item.attributes),
                        })
                    stop_report = device_reader.generate_stop_report(
                        locations,
                        tr['initial_timestamp'],
                        tr['final_timestamp'],
                        0
                    )
                    stop_duration = 0
                    for sr in stop_report:
                        stop_duration += sr['duration']
                    tr['stopped_time'] = str(timedelta(seconds=stop_duration))
                    total_stop_duration += stop_duration
                    tr['driving_time'] = str(timedelta(seconds=(tr['duration']-stop_duration)))
                
                if len(unit_trip_report) != 0:
                    driving_duration = duration - total_stop_duration
                    summarization.append({
                        "unit_name" : unit.name,
                        "unit_description": unit.description,
                        "number_of_trips": number_of_trips,
                        "distance": distance,
                        "duration": duration,
                        "time": str(timedelta(seconds=duration)),
                        "driving_time": str(timedelta(seconds=driving_duration)),
                        "stopped_time": str(timedelta(seconds=total_stop_duration))
                    })
            
            # CALCULAR GEOCERCAS
            geofences = Geofence.objects.filter(account=request.user.profile.account)
            for tr in group_trip_report:
                matching_initial_geofences = []
                matching_final_geofences = []
                for geofence in geofences:
                    feature = json.loads(geofence.geojson)['features'][0]
                    s = shape(feature['geometry'])
                    point = Point(tr['initial_longitude'],tr['initial_latitude'])
                    if s.contains(point):
                        matching_initial_geofences.append(geofence.name)
                    point = Point(tr['final_longitude'],tr['final_latitude'])
                    if s.contains(point):
                        matching_final_geofences.append(geofence.name)
                s_str = ""
                for i in range(len(matching_initial_geofences)):
                    if i==0:
                        s_str += matching_initial_geofences[i]
                    else:
                        s_str += f', {matching_initial_geofences[i]}'
                tr['initial_geofences'] = s_str
                d_str = ""
                for i in range(len(matching_final_geofences)):
                    if i==0:
                        d_str += matching_final_geofences[i]
                    else:
                        d_str += f', {matching_final_geofences[i]}'
                tr['final_geofences'] = d_str
            # FIN - CALCULAR GEOCERCAS
            return render(request,'reports/group-trip-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'group_trip_report':group_trip_report,
                'summarization':summarization,
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

@api_view(['GET'])
def get_stop_report(request,unit_name,initial_datetime,final_datetime,discard_time):
    initial_timestamp = None
    final_timestamp = None
    unit = None
    if unit_name.upper() != 'ALL':
        try:
            unit = Device.objects.get(
                name=unit_name,
                account=request.user.profile.account
            )
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    
    # tiempo para descartar
    seconds = int(discard_time) * 60
    # fin - tiempo para descartar

    stop_report = []
    summarization = []

# STOP REPORT
@login_required
def stop_report_view(request):
    # verificar privilegios
    if privilege.view_stop_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
        initial_timestamp = None
        final_timestamp = None
        form = StopReportForm(data)
        if form.is_valid():
            unit = None
            if data['unit_name'].upper() != 'ALL':
                try:
                    unit = Device.objects.get(name=data['unit_name'])
                except Exception as e:
                    print(e)
                    form.add_error('unit_name', e)
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
            # tiempo para descartar
            seconds = int(data['stopped_time']) * 60
            # fin - tiempo para descartar

            if len(form.errors) != 0:
                return render(request,'reports/stop-report.html',{
                    'units':units,
                    'form':form,
                })

            # Aqui va la logica del resultado
            stop_report = []
            summarization = []
            if data['unit_name'].upper() == 'ALL':
                for unit in units:
                    locations_qs = Location.objects.using('history_db_replica').filter(
                        unitid=unit.id,
                        timestamp__gte=initial_timestamp,
                        timestamp__lt=final_timestamp
                    ).order_by('timestamp')
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
                    device_reader = DeviceReader(unit.uniqueid)
                    unit_stop_report = device_reader.generate_stop_report(locations,initial_timestamp,final_timestamp,seconds)
                    # CALCULAR EL RESUMEN Y AÑADIR LA DESCRIPCION DE LA UNIDAD
                    count = 0
                    for item in unit_stop_report:
                        item['unit_name'] = unit.name
                        item['unit_description'] = unit.description
                        stop_report.append(item)
                        count += 1
                    if count > 0:
                        summarization.append({
                            'unit_name':unit.name,
                            'unit_description':unit.description,
                            'count':count,
                        })
                    # FIN - CALCULAR EL RESUMEN Y AÑADIR LA DESCRIPCION DE LA UNIDAD
            else:
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
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
                device_reader = DeviceReader(unit.uniqueid)
                unit_stop_report = device_reader.generate_stop_report(locations,initial_timestamp,final_timestamp,seconds)
                for item in unit_stop_report:
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    stop_report.append(item)
                # CALCULAR EL RESUMEN
                count = len(unit_stop_report)
                if count > 0:
                    summarization.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'count':count,
                    })
                # FIN - CALCULAR EL RESUMEN
            # CALCULAR GEOCERCAS
            geofences = Geofence.objects.filter(account=request.user.profile.account)
            for sr in stop_report:
                matching_geofences = []
                for geofence in geofences:
                    feature = json.loads(geofence.geojson)['features'][0]
                    s = shape(feature['geometry'])
                    point = Point(sr['longitude'],sr['latitude'])
                    if s.contains(point):
                        matching_geofences.append(geofence.name)
                time.sleep(0.01) #QUE RESPIRE EL SERVER
                c_str = ""
                for i in range(len(matching_geofences)):
                    if i==0:
                        c_str += matching_geofences[i]
                    else:
                        c_str += f', {matching_geofences[i]}'
                sr['geofences'] = c_str
            # FIN - CALCULAR GEOCERCAS
            if len(stop_report) == 0:
                return render(request,'reports/stop-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':unit,
                    'units':units,
                    'form':form,
                    'error':'No existen datos para mostrar.',
                })
            return render(request,'reports/stop-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'stop_report':stop_report,
                'summarization':summarization,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })      
        return render(request,'reports/stop-report.html',{
            'units':units,
            'form':form,
        })
    # GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/stop-report.html',{
        'units':units,
    })

# GROUP STOP REPORT
@login_required
def group_stop_report_view(request):
    # verificar privilegios
    if privilege.view_group_stop_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        groups = Group.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = GroupStopReportForm(data)
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

            # tiempo para descartar
            seconds = int(data['stopped_time']) * 60
            # fin - tiempo para descar

            if len(form.errors) != 0:
                return render(request,'reports/group-stop-report.html',{
                    'groups':groups,
                    'form':form,
                })
            
            group_stop_report = []
            summarization = []

            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('timestamp').exclude(latitude=0.0,longitude=0.0)
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
                device_reader = DeviceReader(unit.uniqueid)
                unit_stop_report = device_reader.generate_stop_report(locations,initial_timestamp,final_timestamp,seconds)
                # CALCULAR EL RESUMEN Y AÑADIR LA DESCRIPCION DE LA UNIDAD
                count = 0
                for item in unit_stop_report:
                    item['group_name'] = group.name
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    group_stop_report.append(item)
                    count += 1
                if count > 0:
                    summarization.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'count':count,
                    })
                # FIN - CALCULAR EL RESUMEN Y AÑADIR LA DESCRIPCION DE LA UNIDAD

            # CALCULAR GEOCERCAS
            geofences = Geofence.objects.filter(account=request.user.profile.account)
            for sr in group_stop_report:
                matching_geofences = []
                for geofence in geofences:
                    feature = json.loads(geofence.geojson)['features'][0]
                    s = shape(feature['geometry'])
                    point = Point(sr['longitude'],sr['latitude'])
                    if s.contains(point):
                        matching_geofences.append(geofence.name)
                time.sleep(0.01) #QUE RESPIRE EL SERVER
                c_str = ""
                for i in range(len(matching_geofences)):
                    if i==0:
                        c_str += matching_geofences[i]
                    else:
                        c_str += f', {matching_geofences[i]}'
                sr['geofences'] = c_str
            # FIN - CALCULAR GEOCERCAS

            return render(request,'reports/group-stop-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'group_name':group.name,
                'group_stop_report':group_stop_report,
                'summarization':summarization,
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

@api_view(['GET'])
def get_speed_report(request,unit_name,initial_datetime,final_datetime,speed_limit):
    initial_timestamp = None
    final_timestamp = None
    unit = None
    if unit_name.upper() != 'ALL':
        try:
            unit = Device.objects.get(name=unit_name,account=request.user.profile.account)
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    
    # Aqui va la logica del resultado
    speed_report = []
    summarization = []

    if unit_name.upper() == 'ALL':
        units = privilege.get_units(request.user.profile)
        for unit in units:
            number_of_speeds = 0
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
            locations = []
            for location_qs in locations_qs:
                locations.append({
                    'latitude':location_qs.latitude,
                    'longitude':location_qs.longitude,
                    'timestamp':location_qs.timestamp,
                    'altitude':location_qs.altitude,
                    'angle':location_qs.angle,
                    'speed':location_qs.speed,
                    'address':location_qs.address,
                    'attributes':json.loads(location_qs.attributes),
                })
            device_reader = DeviceReader(unit.uniqueid)
            speed_limit = int(speed_limit)
            unit_speed_report = device_reader.generate_speed_report(locations,speed_limit)
            for item in unit_speed_report:
                item['unit_name'] = unit.name
                item['unit_description'] = unit.description
                number_of_speeds += 1
                speed_report.append(item)
            if number_of_speeds > 0:
                summarization.append({
                    'unit_name': unit.name,
                    'unit_description': unit.description,
                    'initial_datetime':initial_datetime,
                    'final_datetime':final_datetime,
                    'number_of_speeds': number_of_speeds
                })
    else:
        number_of_speeds = 0
        locations_qs = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        locations = []
        for location_qs in locations_qs:
            locations.append({
                'latitude':location_qs.latitude,
                'longitude':location_qs.longitude,
                'timestamp':location_qs.timestamp,
                'altitude':location_qs.altitude,
                'angle':location_qs.angle,
                'speed':location_qs.speed,
                'address':location_qs.address,
                'attributes':json.loads(location_qs.attributes),
            })
        device_reader = DeviceReader(unit.uniqueid)
        speed_limit = int(speed_limit)
        unit_speed_report = device_reader.generate_speed_report(locations,speed_limit)
        for item in unit_speed_report:
            item['unit_name'] = unit.name
            item['unit_description'] = unit.description
            number_of_speeds += 1
            speed_report.append(item)
        summarization.append({
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime':initial_datetime,
            'final_datetime':final_datetime,
            'number_of_speeds': number_of_speeds
        })

    data = {
        'speed_report': speed_report,
        'summarization': summarization
    }
    
    return Response(data,status=status.HTTP_200_OK)

# REPORTE DE VELOCIDAD
@login_required
def speed_report_view(request):
    # verificar privilegios
    if privilege.view_speed_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
        initial_timestamp = None
        final_timestamp = None
        form = SpeedReportForm(data)
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
                print(e)
                form.add_error('final_datetime', e)
            if len(form.errors) != 0:
                return render(request,'reports/speed-report.html',{
                    'units':units,
                    'form':form,
                })
            # Aqui va la logica del resultado
            speed_report = []
            if data['unit_name'].upper() == 'ALL':
                for unit in units:
                    locations_qs = Location.objects.using('history_db_replica').filter(
                        unitid=unit.id,
                        timestamp__gte=initial_timestamp,
                        timestamp__lt=final_timestamp
                    ).order_by('timestamp')
                    locations_qs = locations_qs.exclude(latitude=0.0,longitude=0.0)
                    locations = []
                    for location_qs in locations_qs:
                        locations.append({
                            'latitude':location_qs.latitude,
                            'longitude':location_qs.longitude,
                            'timestamp':location_qs.timestamp,
                            'angle':location_qs.angle,
                            'altitude':location_qs.altitude,
                            'speed':location_qs.speed,
                            'address':location_qs.address,
                            'attributes':json.loads(location_qs.attributes),
                        })
                    device_reader = DeviceReader(unit.uniqueid)
                    speed_limit = int(data['speed_limit'])
                    unit_speed_report = device_reader.generate_speed_report(locations,speed_limit)
                    for item in unit_speed_report:
                        item['unit_name'] = unit.name
                        item['unit_description'] = unit.description
                        speed_report.append(item) 
            else:
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('id')
                locations_qs = locations_qs.order_by('timestamp')
                locations = []
                for location_qs in locations_qs:
                    locations.append({
                        'latitude':location_qs.latitude,
                        'longitude':location_qs.longitude,
                        'timestamp':location_qs.timestamp,
                        'angle':location_qs.angle,
                        'altitude':location_qs.altitude,
                        'speed':location_qs.speed,
                        'address':location_qs.address,
                        'attributes':json.loads(location_qs.attributes),
                    })
                device_reader = DeviceReader(unit.uniqueid)
                speed_limit = int(data['speed_limit'])
                unit_speed_report = device_reader.generate_speed_report(locations,speed_limit)
                for item in unit_speed_report:
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    speed_report.append(item)
            if len(speed_report) == 0:
                return render(request,'reports/speed-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'speed_limit':data['speed_limit'],
                    'selected_unit':unit,
                    'units':units,
                    'form':form,
                    'error':'No existen datos para mostrar.',
                })
            return render(request,'reports/speed-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'speed_limit':data['speed_limit'],
                'selected_unit':unit,
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
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/speed-report.html',{
        'units':units,
    })

# GROUP SPEED REPORT
@login_required
def group_speed_report_view(request):
    # verificar privilegios
    if privilege.view_group_speed_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
                    timestamp__lt=final_timestamp
                ).order_by('id')
                locations_qs = locations_qs.order_by('timestamp')
                locations = []
                for location_qs in locations_qs:
                    locations.append({
                        'latitude':location_qs.latitude,
                        'longitude':location_qs.longitude,
                        'timestamp':location_qs.timestamp,
                        'angle':location_qs.angle,
                        'altitude':location_qs.altitude,
                        'speed':location_qs.speed,
                        'address':location_qs.address,
                        'attributes':json.loads(location_qs.attributes),
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

@api_view(['GET'])
def get_mileage_report(request,unit_name,initial_datetime,final_datetime):
    unit = None
    if unit_name.upper() != 'ALL':
        try:
            unit = Device.objects.get(name=unit_name,account=request.user.profile.account)
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

    # Aqui va la logica del resultado
    result1 = []
    result2 = []
    if unit_name.upper() == 'ALL':
        units = privilege.get_units(request.user.profile)
        for unit in units:
            initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
            initial_datetime_obj = initial_datetime_obj.replace(hour=0,minute=0,second=0)
            final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
            datetime_ranges = []
            total_distance = 0.0
            while initial_datetime_obj < final_datetime_obj:
                datetime_ranges.append([
                    initial_datetime_obj,
                    initial_datetime_obj+timedelta(days=1)
                ])
                initial_datetime_obj = initial_datetime_obj+timedelta(days=1)
            datetime_ranges[0][0] = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
            datetime_ranges[len(datetime_ranges)-1][1] = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
            for dr in datetime_ranges:
                timestamp1 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[0])))
                timestamp2 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[1])))
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=timestamp1,
                    timestamp__lt=timestamp2
                ).order_by('timestamp')
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
                device_reader = DeviceReader(unit.uniqueid)
                distance_sum = device_reader.generate_mileage_report(locations)
                result2.append({
                    'unit_name':unit.name,
                    'unit_description':unit.description,
                    'initial_datetime':dr[0].strftime("%Y-%m-%d, %H:%M:%S"),
                    'final_datetime':dr[1].strftime("%Y-%m-%d, %H:%M:%S"),
                    'distance':round(distance_sum,2)
                })
                total_distance += distance_sum
            result1.append(
                {
                    "unit_name":unit.name,
                    "unit_description":unit.description,
                    "initial_date":initial_datetime,
                    "final_date":final_datetime,
                    "distance":round(total_distance,2),
                    "odometer":round(unit.odometer,2),
                }
            )
    else:
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        initial_datetime_obj = initial_datetime_obj.replace(hour=0,minute=0,second=0)
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        datetime_ranges = []
        total_distance = 0.0
        while initial_datetime_obj < final_datetime_obj:
            datetime_ranges.append([
                initial_datetime_obj,
                initial_datetime_obj+timedelta(days=1)
            ])
            initial_datetime_obj = initial_datetime_obj+timedelta(days=1)
        datetime_ranges[0][0] = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        datetime_ranges[len(datetime_ranges)-1][1] = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        for dr in datetime_ranges:
            timestamp1 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[0])))
            timestamp2 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[1])))
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=timestamp1,
                timestamp__lt=timestamp2
            ).order_by('timestamp')
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
            device_reader = DeviceReader(unit.uniqueid)
            distance_sum = device_reader.generate_mileage_report(locations)
            result2.append({
                'unit_name':unit.name,
                'unit_description':unit.description,
                'initial_datetime':dr[0].strftime("%Y-%m-%d, %H:%M:%S"),
                'final_datetime':dr[1].strftime("%Y-%m-%d, %H:%M:%S"),
                'distance':round(distance_sum,2)
            })
            total_distance += distance_sum
        result1.append(
            {
                "unit_name":unit.name,
                "unit_description":unit.description,
                "initial_date":initial_datetime,
                "final_date":final_datetime,
                "distance":round(total_distance,2),
                "odometer":round(unit.odometer,2),
            }
        )
    response = {
        'total_mileage':result1,
        'mileage_by_date':result2
    }
    return Response(response,status=status.HTTP_200_OK)
    
# MILEAGE REPORT
@login_required
def mileage_report_view(request):
    # verificar privilegios
    if privilege.view_mileage_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
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
            # Aqui va la logica del resultado
            result = []
            if data['unit_name'].upper() == 'ALL':
                for unit in units:
                    locations_qs = Location.objects.using('history_db_replica').filter(
                        unitid=unit.id,
                        timestamp__gte=initial_timestamp,
                        timestamp__lt=final_timestamp
                    ).order_by('timestamp')
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
                    device_reader = DeviceReader(unit.uniqueid)
                    distance_sum = device_reader.generate_mileage_report(locations)
                    result.append(
                        {
                            "unit_name":unit.name,
                            "unit_description":unit.description,
                            "initial_date":data['initial_datetime'],
                            "final_date":data['final_datetime'],
                            "distance":round(distance_sum,2),
                            "odometer":round(unit.odometer,2),
                        }
                    )
            else:
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('timestamp')
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
                device_reader = DeviceReader(unit.uniqueid)
                distance_sum = device_reader.generate_mileage_report(locations)
                result.append(
                    {
                        "unit_name":unit.name,
                        "unit_description":unit.description,
                        "initial_date":data['initial_datetime'],
                        "final_date":data['final_datetime'],
                        "distance":round(distance_sum,2),
                        "odometer":round(unit.odometer,2),
                    }
                )
            if len(result) == 0:
                return render(request,'reports/mileage-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':unit,
                    'units':units,
                    'form':form,
                    'error':'No existen datos para mostrar.',
                })
            return render(request,'reports/mileage-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'result':result,
                'units':units,
                'form':form,
            })
        return render(request,'reports/mileage-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = privilege.get_units(request.user.profile)
    form = MileageReportForm()
    return render(request,'reports/mileage-report.html',{
        'units':units,
        'form':form,
    })

# GROUP MILEAGE REPORT
@login_required
def group_mileage_report_view(request):
    if privilege.view_group_mileage_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
                    timestamp__lt=final_timestamp
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
    # verificar privilegios
    if privilege.view_geofence_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        geofences = Geofence.objects.filter(account=request.user.profile.account)
        units = privilege.get_units(request.user.profile)
        initial_timestamp = None
        final_timestamp = None
        form = GeofenceReportForm(data)
        if form.is_valid():
            unit = None
            if data['unit_name'].upper() != 'ALL':
                try:
                    unit = Device.objects.get(name=data['unit_name'])
                except Exception as e:
                    print(e)
                    form.add_error('unit_name', e)
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

            try:
                geofence_list = data.getlist('geofence_name')
            except Exception as e:
                form.add_error('geofence_name', e)

            if len(form.errors) != 0:
                return render(request,'reports/geofence-report.html',{
                    'units':units,
                    'geofences':geofences,
                    'form':form,
                })

            # Aqui va la logica del resultado
            geofence_report = []
            if data['unit_name'].upper() == 'ALL':
                for unit in units:
                    locations_qs = Location.objects.using('history_db_replica').filter(
                        unitid=unit.id,
                        timestamp__gte=initial_timestamp,
                        timestamp__lt=final_timestamp
                    ).order_by('timestamp')
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
                    device_reader = DeviceReader(unit.uniqueid)
                    geofences_qs = []
                    for i in range(len(geofence_list)):
                        try:
                            geofence = geofences.get(name=geofence_list[i])
                            geofences_qs.append(geofence)
                        except Exception as e:
                            print(e)
                    unit_geofence_report = device_reader.generate_geofence_report(locations,geofences_qs,initial_timestamp,final_timestamp)
                    for item in unit_geofence_report:
                        item['unit_name'] = unit.name
                        item['unit_description'] = unit.description
                        geofence_report.append(item)
            else:
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
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
                        'geofences':geofences,
                        'form':form,
                        'error':'No existe un recorrido para analizar.'
                    })
                device_reader = DeviceReader(unit.uniqueid)
                geofences_qs = []
                for i in range(len(geofence_list)):
                    try:
                        geofence = geofences.get(name=geofence_list[i])
                        geofences_qs.append(geofence)
                    except Exception as e:
                        print(e)
                # Esta funcion recibe un array de queryset en la variable de geocercas
                unit_geofence_report = device_reader.generate_geofence_report(locations,geofences_qs,initial_timestamp,final_timestamp)
                for item in unit_geofence_report:
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    geofence_report.append(item)
            if len(geofence_report) == 0:
                return render(request,'reports/geofence-report.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':unit,
                    'selected_geofences':geofence_list,
                    'geofences':geofences,
                    'units':units,
                    'form':form,
                    'error':'No existen datos para mostrar.',
                })
            return render(request,'reports/geofence-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'geofence_report':geofence_report,
                'selected_geofences':geofence_list,
                'geofences':geofences,
                'units':units,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })
        return render(request,'reports/geofence-report.html',{
            'units':units,
            'geofences':geofences,
            'form':form,
        })

    #GET
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    units = privilege.get_units(request.user.profile)
    form = ReportForm()
    return render(request,'reports/geofence-report.html',{
        'units':units,
        'geofences':geofences,
        'form':form,
    })

@api_view(['POST'])
def get_geofence_report(request):
    data = request.data
    serializer = GeofenceReportSerializer(data=data)
    if serializer.is_valid():
        if data['unit_name'].upper() != 'ALL':
            try:
                unit = Device.objects.get(name=data['unit_name'],account=request.user.profile.account)
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        #
        initial_datetime_str = data['initial_datetime']
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = data['final_datetime']
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
        #
        if final_timestamp - initial_timestamp > 259200:
            error = {
                'detail': 'Report time range exceeded.'
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
        geofence_report = []
        if data['unit_name'].upper() == 'ALL':
            units = privilege.get_units(request.user.profile)
            for unit in units:
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('timestamp')
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
                device_reader = DeviceReader(unit.uniqueid)
                geofences_qs = []
                for gqs in data['geofences']:
                    try:
                        geofence = Geofence.objects.get(id=gqs,account=request.user.profile.account)
                        geofences_qs.append(geofence)
                    except:
                        pass
                unit_geofence_report = device_reader.generate_geofence_report(locations,geofences_qs,initial_timestamp,final_timestamp)
                for item in unit_geofence_report:
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    geofence_report.append(item)
        else:
            locations_qs = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
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
            device_reader = DeviceReader(unit.uniqueid)
            geofences_qs = []
            for gqs in data['geofences']:
                try:
                    geofence = Geofence.objects.get(id=gqs,account=request.user.profile.account)
                    geofences_qs.append(geofence)
                except:
                    pass
            unit_geofence_report = device_reader.generate_geofence_report(locations,geofences_qs,initial_timestamp,final_timestamp)
            
            for item in unit_geofence_report:
                item['unit_name'] = unit.name
                item['unit_description'] = unit.description
                geofence_report.append(item)

        return Response(geofence_report,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

# GROUP GEOFENCE REPORT
@login_required
def group_geofence_report_view(request):
    # verificar privilegios
    if privilege.view_geofence_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        geofences = Geofence.objects.filter(account=request.user.profile.account)
        groups = Group.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = GroupGeofenceReportForm(data)
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

            try:
                geofence_list = data.getlist('geofence_name')
            except Exception as e:
                form.add_error('geofence_name', e)

            if len(form.errors) != 0:
                return render(request,'reports/group-geofence-report.html',{
                    'groups':groups,
                    'form':form,
                })

            # Aqui va la logica del resultado
            group_geofence_report = []

            for unit in group.units.all():
                locations_qs = Location.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lt=final_timestamp
                ).order_by('timestamp')
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
                device_reader = DeviceReader(unit.uniqueid)
                geofences_qs = []
                if geofence_list[0].upper() == 'ALL':
                    geofences_qs = geofences
                else:
                    for i in range(len(geofence_list)):
                        try:
                            geofence = geofences.get(name=geofence_list[i])
                            geofences_qs.append(geofence)
                        except Exception as e:
                            print(e)
                unit_geofence_report = device_reader.generate_geofence_report(locations,geofences_qs,initial_timestamp,final_timestamp)
                for item in unit_geofence_report:
                    item['unit_name'] = unit.name
                    item['unit_description'] = unit.description
                    group_geofence_report.append(item)

            return render(request,'reports/group-geofence-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'group_name':group.name,
                'group_geofence_report':group_geofence_report,
                'selected_geofences':geofence_list,
                'geofences':geofences,
                'groups':groups,
                'form':form,
                #'error':'The request was denied due to the limitation of the request. Please wait for Amazon AWS DynamoDB to implement the processing logic.'
            })

        return render(request,'reports/group-geofence-report.html',{
            'groups':groups,
            'geofences':geofences,
            'form':form,
        })

    # GET
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-geofence-report.html',{
        'groups':groups,
        'geofences':geofences,
    })

@login_required
def telemetry_report_view(request):
    # verificar privilegios
    if privilege.view_telemetry_report(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    if request.method == 'POST':
        data = request.POST
        units = privilege.get_units(request.user.profile)
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

            if len(form.errors) != 0:
                return render(request,'reports/detailed-report-with-attributes.html',{
                    'units':units,
                    'form':form,
                })
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=initial_timestamp,
                timestamp__lt=final_timestamp
            ).order_by('timestamp').exclude(
                latitude=0.0,
                longitude=0.0
            )
            fuel_used_offset = 0
            rpm_list = []
            fuel_rate_list = []
            fuel_economy_list = []
            for i in range(len(locations)):
                dt = datetime.utcfromtimestamp(locations[i].timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                locations[i].datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                attributes = json.loads(locations[i].attributes)
                # ignicion
                device_reader = DeviceReader(unit.uniqueid)
                locations[i].ignition = device_reader.detect_ignition_event({
                    'attributes':attributes
                })
                try:
                    locations[i].rpm_engine = attributes['io88']
                    rpm_list.append(int(attributes['io88']))
                except:
                    locations[i].rpm_engine = 'N/D'
                try:
                    locations[i].fuel_rate = attributes['io135']
                    fuel_rate_list.append(int(attributes['io135']))
                except:
                    locations[i].fuel_rate = 'N/D'
                try:
                    locations[i].fuel_economy = attributes['io136']
                    if int(attributes['io136']) != 0:
                        fuel_economy_list.append(int(attributes['io136']))
                except:
                    locations[i].fuel_economy = 'N/D'
                try:
                    locations[i].ambient_temperature = attributes['io128']
                except:
                    locations[i].ambient_temperature = 'N/D'
                try:
                    locations[i].engine_coolant_temperature	= attributes['io127']
                except:
                    locations[i].engine_coolant_temperature = 'N/D'
                try:
                    locations[i].total_fuel_used = attributes['io86']
                except:
                    locations[i].total_fuel_used = 'N/D'
                try:
                    if i == 0:
                        fuel_used_offset = int(attributes['io86'])
                        locations[i].accumulated_fuel = 0
                    else:
                        locations[i].accumulated_fuel = int(attributes['io86']) - fuel_used_offset
                except:
                    locations[i].accumulated_fuel = 'N/D'
                try:
                    locations[i].odometer = round(float(attributes['io192'])/1000,2)
                except:
                    locations[i].odometer = 'N/D'
            try:
                summarization = [
                    {
                        'unit_name': unit.name,
                        'unit_description': unit.description,
                        'maximum_rpm': max(rpm_list),
                        'maximum_fuel_rate': max(fuel_rate_list),
                        'average_fuel_economy': sum(fuel_economy_list)/len(fuel_economy_list),
                        'mileage': locations[len(locations)-1].odometer - locations[0].odometer,
                    }
                ]
            except Exception as e:
                print(e)
                summarization = []
            return render(request,'reports/telemetry-report.html',{
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'selected_unit':unit,
                'units':units,
                'locations':locations,
                'summarization':summarization,
            })
        return render(request,'reports/telemetry-report.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/telemetry-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_telemetry_report(request):
    data = request.data
    serializer = ReportSerializer(data=data)
    if serializer.is_valid():
        if data['unit_name'].upper() != 'ALL':
            try:
                unit = Device.objects.get(name=data['unit_name'],account=request.user.profile.account)
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        #
        initial_datetime_str = data['initial_datetime']
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = data['final_datetime']
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
        #
        if final_timestamp - initial_timestamp > 604800:
            error = {
                'detail': 'Report time range exceeded.'
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )

        telemetry_report = []
        summarization = []
        rpm_list = []
        engine_coolant_temp_list = []
        ambient_air_temp_list = []
        acceleration_pedal_position_list = []
        engine_current_load_list = []
        engine_total_fuel_used_list = []

        device_reader = DeviceReader(unit.uniqueid)
        for i in range(len(locations)):
            dt = datetime.utcfromtimestamp(locations[i].timestamp)
            dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
            attributes = json.loads(locations[i].attributes)
            item = {
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': dt.strftime("%d/%m/%Y %H:%M:%S"),
                'latitude': locations[i].latitude,
                'longitude': locations[i].longitude,
                'speed': locations[i].speed,
                'ignition': device_reader.detect_ignition_event({
                    'attributes':json.loads(locations[i].attributes)
                }),
                'address': locations[i].address,
            }
            try:
                if locations[i].protocol == 'teltonika640':
                    item['rpm_engine'] = attributes['io88']
                    rpm_list.append(attributes['io88'])
                else:
                    item['rpm_engine'] = 'N/D'
            except Exception as e:
                item['rpm_engine'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['engine_coolant_temp'] = attributes['io127']
                    engine_coolant_temp_list.append(attributes['io127'])
                else:
                    item['engine_coolant_temp'] = 'N/D'
            except Exception as e:
                item['engine_coolant_temp'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['ambient_air_temp'] = attributes['io128']
                    ambient_air_temp_list.append(attributes['io128'])
                else:
                    item['ambient_air_temp'] = 'N/D'
            except Exception as e:
                item['ambient_air_temp'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['odometer'] = round(attributes['io192']/1000,2)
                else:
                    item['odometer'] = 'N/D'
            except Exception as e:
                item['odometer'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['acceleration_pedal_position'] = attributes['io84']
                    acceleration_pedal_position_list.append(attributes['io84'])
                else:
                    item['acceleration_pedal_position'] = 'N/D'
            except Exception as e:
                item['acceleration_pedal_position'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['engine_current_load'] = attributes['io85']
                    engine_current_load_list.append(attributes['io85'])
                else:
                    item['engine_current_load'] = 'N/D'
            except Exception as e:
                item['engine_current_load'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['engine_total_fuel_used'] = attributes['io86']
                    engine_total_fuel_used_list.append(attributes['io86'])
                else:
                    item['engine_total_fuel_used'] = 'N/D'
            except Exception as e:
                item['engine_total_fuel_used'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['fuel_level'] = attributes['io87']
                else:
                    item['fuel_level'] = 'N/D'
            except Exception as e:
                item['fuel_level'] = 'N/D'
            
            telemetry_report.append(item)
            
        if len(telemetry_report) > 0:
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'max_rpm': max(rpm_list),
                'max_engine_coolant_temp': max(engine_coolant_temp_list),
                'max_ambient_air_temp': max(ambient_air_temp_list),
                'max_acceleration_pedal_position': max(acceleration_pedal_position_list),
                'max_engine_current_load': max(engine_current_load_list),
                'fuel_used': max(engine_total_fuel_used_list) - min(engine_total_fuel_used_list),
            })  
        final_report = {
            'telemetry_report':telemetry_report,
            'summarization':summarization,
        }    
        return Response(final_report,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def temperature_report_view(request):
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/temperature-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_temperature_report(request):
    data = request.data
    serializer = ReportSerializer(data=data)
    if serializer.is_valid():
        if data['unit_name'].upper() != 'ALL':
            try:
                unit = Device.objects.get(name=data['unit_name'],account=request.user.profile.account)
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        #
        initial_datetime_str = data['initial_datetime']
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = data['final_datetime']
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
        #
        if final_timestamp - initial_timestamp > 604800:
            error = {
                'detail': 'Report time range exceeded.'
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )

        temperature_report = []
        summarization = []
        temp_list = []

        device_reader = DeviceReader(unit.uniqueid)
        for location in locations:
            dt = datetime.utcfromtimestamp(location.timestamp)
            dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
            item = {
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': dt.strftime("%d/%m/%Y %H:%M:%S"),
                'latitude': location.latitude,
                'longitude': location.longitude,
                'speed': location.speed,
                'ignition': device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                }),
                'address': location.address,
            }
            try:
                temp = float(json.loads(location.attributes)['temp1'])/0.1
                if int(temp) == 3000:
                    item['temp'] = int(temp)
                    temperature_report.append(item)
                    temp_list.append(int(temp))
                else:
                    item['temp'] = round(temp*0.001,2)
                    temperature_report.append(item)
                    temp_list.append(round(temp*0.001,2))
            except Exception as e:
                pass
            
        if len(temp_list) > 0:
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'max_temp': max(temp_list),
                'min_temp': min(temp_list),
                'avg1_temp': round(mean(temp_list),2),
                'avg2_temp': round(median(temp_list),2)
            })  
        final_report = {
            'temperature_report':temperature_report,
            'summarization':summarization,
        }    
        return Response(final_report,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def hours_report_view(request):
    #GET
    units = privilege.get_units(request.user.profile)
    return render(request,'reports/hours-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_hours_report(request):
    data = request.data
    serializer = ReportSerializer(data=data)
    if serializer.is_valid():
        if data['unit_name'].upper() != 'ALL':
            try:
                unit = Device.objects.get(name=data['unit_name'],account=request.user.profile.account)
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        #
        initial_datetime_str = data['initial_datetime']
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        #
        final_datetime_str = data['final_datetime']
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
        #
        if final_timestamp - initial_timestamp > 604800:
            error = {
                'detail': 'Report time range exceeded.'
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )

        hours_report = []
        summarization = []
        hours_list = []
        device_reader = DeviceReader(unit.uniqueid)
        for location in locations:
            dt = datetime.utcfromtimestamp(location.timestamp)
            dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
            item = {
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': dt.strftime("%d/%m/%Y %H:%M:%S"),
                'latitude': location.latitude,
                'longitude': location.longitude,
                'speed': location.speed,
                'ignition': device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                }),
                'address': location.address,
            }
            try:
                c_time = int(device_reader.get_hours({'attributes':json.loads(location.attributes)}))
                #c_time = int(json.loads(location.attributes)['io449'])
                if c_time > 0:
                    hours = int(c_time/3600)
                    minutes = int(c_time%3600/60)
                    item['hours'] = f"{hours} h {minutes} m"
                    hours_report.append(item)
                    hours_list.append(c_time)
            except Exception as e:
                print(e)
                pass
        if len(hours_list) > 0:
            c_time = max(hours_list) - min(hours_list)
            hours = int(c_time/3600)
            minutes = int(c_time%3600/60)
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime':data['initial_datetime'],
                'final_datetime':data['final_datetime'],
                'hours': f"{hours} h {minutes} m",
            })
        final_report = {
            'hours_report':hours_report,
            'summarization':summarization,
        } 
        return Response(final_report,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)