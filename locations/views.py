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
from time import sleep
from datetime import datetime
from geopy.distance import great_circle
from asgiref.sync import async_to_sync

from .models import Location,SutranLocation,PanderoLocation
from units.models import Device
from .serializers import InsertLocationSerializer,LocationSerializer,InsertLocationSerializer2
from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader
from common.alert_reader import AlertReader
from .tasks import insert_location_in_history,process_alert

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria

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
                # CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
                ts = int(datetime.now().timestamp())
                ts_offset = ts - data['timestamp']
                if ts_offset > 31536000: data['timestamp'] = ts
                # FIN CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
                unit.last_timestamp = data['timestamp']
                unit.last_latitude = data['latitude']
                unit.last_longitude = data['longitude']
                unit.last_altitude = data['altitude']
                unit.last_angle = data['angle']
                unit.last_speed = data['speed']
                if int(data['speed']) > 0:
                    unit.last_movement = unit.last_timestamp = data['timestamp']
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
                # INSERTAR UBICACION EN EL HISTORICO
                data['unit_id'] = unit.id
                data['unit_name'] = unit.name
                data['account'] = unit.account.name
                insert_location_in_history.delay(data)

                # ALERTAS
                process_alert.delay(data)
                # FIN - ALERTAS

                # ACTUALIZAR UNIDADES EN EL MAPA
                account = unit.account.name
                last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data['timestamp']))
                last_report = last_report.strftime("%d/%m/%Y, %H:%M:%S")
                channel_layer = channels.layers.get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    f'chat_{account}',
                    {
                        'type': 'send_message',
                        'message': {
                            'type':'update_location',
                            'payload': {
                                'unitid': unit.id,
                                'unit_name': unit.name,
                                'unit_description': unit.description,
                                'timestamp': data['timestamp'],
                                'latitude': data['latitude'],
                                'longitude': data['longitude'],
                                'altitude': data['altitude'],
                                'angle': data['angle'],
                                'speed': data['speed'],
                                'attributes': data['attributes'],
                                'address': data['address'],
                                'odometer': round(unit.odometer,2),
                                'last_report': last_report
                            }
                        }
                    }
                )
                # FIN - ACTUALIZAR UNIDADES EN EL MAPA
                #sleep(0.001)
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
        api_url = f'http://{GEOCODING_SERVER}:{GEOCODING_PORT}/nominatim/reverse?format=jsonv2&lat={latitude}&lon={longitude}&addressdetails=1'
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
    serializer = LocationSerializer(locations,many=True)
    data = serializer.data
    data1 = []
    for i in range(len(data)):
        if data[i]['latitude'] != 0.0 and data[i]['longitude'] != 0.0:
            data[i]['unit_name'] = unit_name
            data[i]['attributes'] = json.loads(data[i]['attributes'])
            last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data[i]['timestamp']))
            data[i]['datetime'] = last_report.strftime("%d/%m/%Y, %H:%M:%S")
            data1.append(data[i])   
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

@api_view(['POST'])
def insert_history_location_batch(request):
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
                # INSERTAR UBICACION EN EL HISTORICO
                data['unit_id'] = unit.id
                data['unit_name'] = unit.name
                data['account'] = unit.account.name
                insert_location_in_history.delay(data)

                # ALERTAS
                #process_alert.delay(data)
                # FIN - ALERTAS
        else:
            errors = {
                'errors':serializer.errors
            }
            return Response(errors)
    if len(error_list) != 0:
        return Response(error_list)
    return Response([])   

@api_view(['POST'])
def insert_sutran_location(request):
    data = request.data
    serializer = InsertLocationSerializer(data=data)
    if serializer.is_valid():
        pass