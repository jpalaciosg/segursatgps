from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import websocket
import json
import channels.layers
import requests
from asgiref.sync import async_to_sync

from .models import Location
from .serializers import LocationSerializer
from units.models import Unit

WS_TARGET = '127.0.0.1'
WS_PORT = 8000
GEOCODING_SERVER = '172.16.2.4'

# Create your views here.
@api_view(['POST'])
def insert_location(request):
    data = request.data
    serializer = LocationSerializer(data=data)
    if serializer.is_valid():
        try:
            deviceid = data['deviceid']
            unit = Unit.objects.get(device__uniqueid=deviceid)
        except Exception as e:
            error = {'error':str(e)}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        unit.device.last_timestamp = data['timestamp']
        unit.device.last_latitude = data['latitude']
        unit.device.last_longitude = data['longitude']
        unit.device.last_altitude = data['altitude']
        unit.device.last_angle = data['angle']
        unit.device.last_speed = data['speed']
        unit.device.last_attributes = json.dumps(data['attributes'])
        try:
            api_url = f"http://{GEOCODING_SERVER}/nominatim/reverse?format=jsonv2&lat={data['latitude']}&lon={data['longitude']}&addressdetails=1"
            headers = {'Content-Type': 'application/json'}
            response = requests.get(api_url, headers=headers)
            address = json.loads(response.content.decode('utf-8'))['display_name']
        except Exception as e:
            address = ""
        unit.device.last_address = address
        unit.device.save()
        location = Location.objects.create(
            unit_name = unit.name,
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
                'type': 'update_location',
                'message': {
                    'unit_name': location.unit_name,
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
        )
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