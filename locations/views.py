from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import websocket
import json
import channels.layers
import requests
import redis
from datetime import datetime
from geopy.distance import great_circle
from asgiref.sync import async_to_sync

from .models import Location,SutranLocation,PanderoLocation
from units.models import Device
from .serializers import InsertLocationSerializer,LocationSerializer,InsertLocationSerializer2
from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader
from common.alert_reader import AlertReader
from .config import GEOCODING_SERVER,GEOCODING_PORT,TARGETS

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria

@api_view(['POST'])
def insert_location(request):
    data = request.data
    serializer = InsertLocationSerializer(data=data)
    if serializer.is_valid():
        try:
            deviceid = data['deviceid']
            unit = Device.objects.get(uniqueid=deviceid)
            previous_location = {
                'timestamp':unit.last_timestamp,
                'latitude':unit.last_latitude,
                'longitude':unit.last_longitude,
                'altitude':unit.last_altitude,
                'angle':unit.last_angle,
                'speed':unit.last_speed,
                'attributes':unit.last_attributes,
                'address':unit.last_address
            }
        except Exception as e:
            error = {'error':str(e)}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        unit.last_timestamp = data['timestamp']
        unit.last_latitude = data['latitude']
        unit.last_longitude = data['longitude']
        unit.last_altitude = data['altitude']
        unit.last_angle = data['angle']
        unit.last_speed = data['speed']
        unit.last_attributes = json.dumps(data['attributes'])

        # reenviar a getposition
        try:
            for target in TARGETS:
                if target['enable']:
                    for u in target['units']:
                        if u == unit.name:
                            device_reader = DeviceReader(unit.uniqueid)
                            ignition = device_reader.detect_ignition_event({
                                'attributes':json.loads(unit.last_attributes)
                            })
                            payload = {
                                "provider":target['name'],
                                "unit_name":unit.name,
                                "timestamp":unit.last_timestamp,
                                "latitude":unit.last_latitude,
                                "longitude":unit.last_longitude,
                                "altitude":unit.last_altitude,
                                "angle":unit.last_angle,
                                "speed":unit.last_speed,
                                "ignition":ignition,
                            }
                            redisClient = redis.StrictRedis(host='localhost',port=6379,db=0)
                            redisClient.rpush('tracklogSegursatQueue', json.dumps(payload))
        except Exception as e:
            print(e)
        # fin reenviar a getposition

        # CALCULAR UBICACION PREVIA
        if previous_location['latitude'] != 0.0 and previous_location['longitude'] != 0.0:
            if data['latitude'] != 0.0 and data['longitude'] != 0.0:
                distance = great_circle(
                    (
                        previous_location['latitude'],
                        previous_location['longitude']
                    ),
                    (
                        data['latitude'],
                        data['longitude']
                    ),
                ).km
                unit.odometer += distance
        unit.previous_location = json.dumps(previous_location)
        # FIN CALCULAR UBICACION PREVIA
        try:
            api_url = f"http://{GEOCODING_SERVER}:{GEOCODING_PORT}/nominatim/reverse?format=jsonv2&lat={data['latitude']}&lon={data['longitude']}&addressdetails=1"
            headers = {'Content-Type': 'application/json'}
            response = requests.get(api_url, headers=headers, timeout=5)
            address = json.loads(response.content.decode('utf-8'))['display_name']
        except Exception as e:
            address = ""
        unit.last_address = address
        unit.save()
        # INSERTAR UBICACION EN EL HISTORICO
        location = Location.objects.create(
            unitid = unit.id,
            protocol= data['protocol'],
            timestamp = data['timestamp'],
            latitude = data['latitude'],
            longitude = data['longitude'],
            altitude = data['altitude'],
            angle = data['angle'],
            speed = data['speed'],
            attributes = json.dumps(data['attributes']),
            address = address,
            reference = unit.name
        )
        # FIN INSERTAR UBICACION EN EL HISTORICO
        account = unit.account.name
        last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(location.timestamp))
        last_report = last_report.strftime("%d/%m/%Y, %H:%M:%S")
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{account}',
            {
                'type': 'send_message',
                'message': {
                    'type':'update_location',
                    'payload': {
                        'unitid': location.unitid,
                        'unit_name': unit.name,
                        'timestamp': location.timestamp,
                        'latitude': location.latitude,
                        'longitude': location.longitude,
                        'altitude': location.altitude,
                        'angle': location.angle,
                        'speed': location.speed,
                        'attributes': data['attributes'],
                        'address': location.address,
                        'odometer': round(unit.odometer,2),
                        'last_report': last_report
                    }
                }
            }
        )
        # ALERTAS
        #alert_reader = AlertReader(unit.uniqueid)
        #alert_reader.run(data)
        # FIN ALERTAS
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def insert_location_batch(request):
    data_list = request.data
    error_list = []
    units = Device.objects.all()
    for data in data_list:
        serializer = InsertLocationSerializer2(data=data)
        if serializer.is_valid():
            deviceid = data['deviceid']
            errors = None
            try:
                unit = units.get(uniqueid=deviceid)
            except Exception as e:
                print(e)
                errors = {
                    'id': data['id'],
                    'errors':{
                        'deviceid':f"El dispositivo {data['deviceid']} no existe"
                    }
                }
                error_list.append(errors)
            
            if errors == None:
                try:
                    attributes = json.loads(unit.last_attributes)
                except Exception as e:
                    attributes = json.loads("{}")
                previous_location = {
                    'timestamp':unit.last_timestamp,
                    'latitude':unit.last_latitude,
                    'longitude':unit.last_longitude,
                    'altitude':unit.last_altitude,
                    'angle':unit.last_angle,
                    'speed':unit.last_speed,
                    'attributes':attributes,
                    'address':unit.last_address
                }
                unit.last_timestamp = data['timestamp']
                unit.last_latitude = data['latitude']
                unit.last_longitude = data['longitude']
                unit.last_altitude = data['altitude']
                unit.last_angle = data['angle']
                unit.last_speed = data['speed']
                unit.last_attributes = json.dumps(data['attributes'])
                # CALCULAR UBICACION PREVIA
                if previous_location['latitude'] != 0.0 and previous_location['longitude'] != 0.0:
                    if data['latitude'] != 0.0 and data['longitude'] != 0.0:
                        distance = great_circle(
                            (
                                previous_location['latitude'],
                                previous_location['longitude']
                            ),
                            (
                                data['latitude'],
                                data['longitude']
                            ),
                        ).km
                        unit.odometer += distance
                unit.previous_location = json.dumps(previous_location)
                # FIN CALCULAR UBICACION PREVIA
                unit.last_address = data['address']
                unit.save()

                # INTRODUCIR UBICACION EN EL HISTORICO
                integrity_error = False
                try:
                    location = Location.objects.create(
                        unitid = unit.id,
                        protocol= data['protocol'],
                        timestamp = data['timestamp'],
                        latitude = data['latitude'],
                        longitude = data['longitude'],
                        altitude = data['altitude'],
                        angle = data['angle'],
                        speed = data['speed'],
                        attributes = json.dumps(data['attributes']),
                        address = data['address'],
                        reference = unit.name
                    )
                except IntegrityError as e:
                    integrity_error = True
                    error_list.append({
                        'id': data['id'],
                        'errors':{
                            'integrity_error': 'Ya existe una ubicación con la misma fecha/hora.'
                        }
                    })
                if unit.account.name == 'leasy':
                    try:
                        location2 = PanderoLocation.objects.create(
                            unitid = unit.id,
                            protocol= data['protocol'],
                            timestamp = data['timestamp'],
                            latitude = data['latitude'],
                            longitude = data['longitude'],
                            altitude = data['altitude'],
                            angle = data['angle'],
                            speed = data['speed'],
                            attributes = json.dumps(data['attributes']),
                            address = data['address'],
                            reference = unit.name
                        )
                    except IntegrityError as e:
                        pass
                # FIN - INTRODUCIR UBICACION EN EL HISTORICO
                # INTRODUCIR UBICACION SUTRAN
                if unit.account.name == 'civa':
                    try:
                        if int(data['speed'] > 0): event = 'EN'
                        else: event = 'PA'
                        timestamp = data['timestamp']
                        device_datetime = datetime.utcfromtimestamp(timestamp)
                        device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
                        sutran_location = SutranLocation.objects.create(
                            unit_name = unit.name,
                            latitude = data['latitude'],
                            longitude = data['longitude'],
                            angle = data['angle'],
                            speed = data['speed'],
                            event = event,
                            device_datetime = device_datetime,
                            server_datetime = gmt_conversor.convert_utctolocaltime(datetime.utcnow()),
                        )
                    except:
                        pass
                      
                # FIN - INTRODUCIR UBICACION SUTRAN
                if integrity_error == False:

                    # ALERTAS
                    alert_reader = AlertReader(unit)
                    alert_reader.run()
                    # FIN - ALERTAS

                    # ACTUALIZAR UNIDADES EN EL MAPA
                    account = unit.account.name
                    last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(location.timestamp))
                    last_report = last_report.strftime("%d/%m/%Y, %H:%M:%S")
                    channel_layer = channels.layers.get_channel_layer()
                    async_to_sync(channel_layer.group_send)(
                        f'chat_{account}',
                        {
                            'type': 'send_message',
                            'message': {
                                'type':'update_location',
                                'payload': {
                                    'unitid': location.unitid,
                                    'unit_name': unit.name,
                                    'timestamp': location.timestamp,
                                    'latitude': location.latitude,
                                    'longitude': location.longitude,
                                    'altitude': location.altitude,
                                    'angle': location.angle,
                                    'speed': location.speed,
                                    'attributes': data['attributes'],
                                    'address': location.address,
                                    'odometer': round(unit.odometer,2),
                                    'last_report': last_report
                                }
                            }
                        }
                    )
                    # FIN - ACTUALIZAR UNIDADES EN EL MAPA
        else:
            errors = {
                'errors':serializer.errors
            }
            return Response(errors)
    if len(error_list) != 0:
        return Response(error_list)
    return Response([])   

@api_view(['GET'])
def get_address(request,latitude,longitude):
    try:
        latitude = float(latitude)
        longitude = float(longitude)
        api_url = f'http://{GEOCODING_SERVER}/nominatim/reverse?format=jsonv2&lat={latitude}&lon={longitude}&addressdetails=1'
        headers = {'Content-Type': 'application/json'}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return Response(json.loads(response.content.decode('utf-8'))['display_name'])
        else:
            return Response(status=400)
    except Exception as e:
        print(e)
        return Response(status=500)

@api_view(['GET'])
def get_location_history(request,unit_name,initial_datetime,final_datetime):
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
    locations = Location.objects.filter(unitid=unit.id,timestamp__gte=initial_timestamp,timestamp__lte=final_timestamp).order_by('timestamp')
    #locations = reversed(locations)
    serializer = LocationSerializer(locations,many=True)
    data = serializer.data
    data1 = []
    for i in range(len(data)):
        data[i]['attributes'] = json.loads(data[i]['attributes'])
        if data[i]['latitude'] != 0.0 and data[i]['longitude'] != 0.0:
            data1.append(data[i])
        data[i]['unit_name'] = unit_name
    return Response(data1,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_location(request,id):
    try:
        location = Location.objects.get(id=id,account=request.user.profile.account)
        serializer = LocationSerializer(location,many=False)
        data = serializer.data
        data['attributes'] = json.loads(data['attributes'])
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_pandero_location_history(request,initial_datetime,final_datetime):
    initial_timestamp = None
    final_timestamp = None
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
    locations = PanderoLocation.objects.filter(timestamp__gte=initial_timestamp,timestamp__lte=final_timestamp).order_by('timestamp')
    serializer = LocationSerializer(locations,many=True)
    data = serializer.data
    data1 = []
    for i in range(len(data)):
        data[i]['attributes'] = json.loads(data[i]['attributes'])
        if data[i]['latitude'] != 0.0 and data[i]['longitude'] != 0.0:
            data1.append(data[i])
        data[i]['unit_name'] = data[i]['reference']
    return Response(data1,status=status.HTTP_200_OK)