from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import websocket
import json
import channels.layers
import requests
from datetime import datetime
from geopy.distance import great_circle
from asgiref.sync import async_to_sync

from .models import Location
from units.models import Device
from .serializers import InsertLocationSerializer,LocationSerializer
from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader
from common.alert_reader import AlertReader

WS_TARGET = '127.0.0.1'
WS_PORT = 8000
GEOCODING_SERVER = '172.16.2.4'

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
            api_url = f"http://{GEOCODING_SERVER}/nominatim/reverse?format=jsonv2&lat={data['latitude']}&lon={data['longitude']}&addressdetails=1"
            headers = {'Content-Type': 'application/json'}
            response = requests.get(api_url, headers=headers, timeout=5)
            address = json.loads(response.content.decode('utf-8'))['display_name']
        except Exception as e:
            address = ""
        unit.last_address = address
        unit.save()
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
            address = address
        )
        account = unit.account.name
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_PRUEBAS',
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
                        'attributes': location.attributes,
                        'address': location.address
                    }
                }
            }
        )
        # ALERTAS
        alert_reader = AlertReader(unit.uniqueid)
        alert_reader.run(data)
        # FIN ALERTAS
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

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
def get_location_history(request,unit_name,initial_date,final_date):
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
        initial_datetime_str = f'{initial_date} 00:00:00'
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
        print(initial_timestamp)
        #
        final_datetime_str = f'{final_date} 00:00:00'
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        final_timestamp = datetime.timestamp(final_datetime_obj)
        final_timestamp = final_timestamp+86400
        print(final_timestamp)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    locations = Location.objects.filter(unitid=unit.id,timestamp__gte=initial_timestamp,timestamp__lte=final_timestamp).order_by('-id')
    locations = reversed(locations)
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