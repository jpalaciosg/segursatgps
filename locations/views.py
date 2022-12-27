from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json
from datetime import datetime,timedelta

from .models import Location,SutranLocation
from units.models import Device
from .serializers import InsertLocationSerializer,LocationSerializer,InsertSutranLocationSerializer,InsertSolgasLocationSerializer
from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader
from common.privilege import Privilege
from .tasks import insert_location_in_history2,process_alert_without_notification,process_location_in_background,process_thirdparty_location_in_background

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

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

@api_view(['POST'])
def insert_history_location_batch(request):
    data_list = request.data
    error_list = []
    units = Device.objects.all()
    for data in data_list:
        serializer = InsertLocationSerializer(data=data)
        if serializer.is_valid():
            #data = serializer.validated_data
            deviceid = data['deviceid']
            errors = None
            try:
                unit = units.get(uniqueid=deviceid)
            except Exception as e:
                print(e)
                errors = {
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
                insert_location_in_history2.delay(data)

                # ALERTAS
                process_alert_without_notification(data)
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
    serializer = InsertSutranLocationSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        server_datetime = datetime.utcnow() - timedelta(hours=5)
        device_datetime = server_datetime + timedelta(seconds=30)
        event = "PA"
        if data['speed'] > 0: event = "EN"
        SutranLocation.objects.create(
            unit_name = data['unit_name'],
            latitude = data['latitude'],
            longitude = data['longitude'],
            angle = data['angle'],
            speed = data['speed'],
            event = event,
            server_datetime = server_datetime,
            device_datetime = device_datetime,
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_async_location_batch(request):
    data_list = request.data
    error_counter = 0
    if len(data_list) == 0:
        response = {'detail':'Payload is empty'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    for data in data_list:
        serializer = InsertLocationSerializer(data=data)
        if serializer.is_valid():
            #data = serializer.validated_data
            if int(data['speed']) < 254:
                process_location_in_background.delay(data)
        else:
            error_counter += 1
    response = {
        'detail':f'Registered ({len(data_list)-error_counter}/{len(data_list)})'
    }
    return Response(response)

@api_view(['POST'])
def insert_async_location(request):
    data = request.data
    serializer = InsertLocationSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        process_location_in_background.delay(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_async_solgas_location(request):
    data = request.data
    serializer = InsertSolgasLocationSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        data['deviceid'] = data['license_plate']
        data['protocol'] = 'generic'
        data['attributes'] = {
            'ignition': data['ignition'],
            'panic': data['panic'],
        }
        del data['license_plate']
        del data['uniqueid']
        del data['ignition']
        del data['panic']
        process_thirdparty_location_in_background.delay(data)
        response = {
            'status':'OK'
        }
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {
            'errors':serializer.errors
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_async_solgas_location_batch(request):
    data_list = request.data
    error_counter = 0
    if len(data_list) == 0:
        response = {'detail':'Payload is empty'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    for data in data_list:
        serializer = InsertSolgasLocationSerializer(data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            data['deviceid'] = data['license_plate']
            data['protocol'] = 'generic'
            data['attributes'] = {
                'ignition': data['ignition'],
                'panic': data['panic'],
            }
            del data['license_plate']
            del data['uniqueid']
            del data['ignition']
            del data['panic']
            process_thirdparty_location_in_background.delay(data)
        else:
            error_counter += 1
    response = {
        'detail':f'Registered ({len(data_list)-error_counter}/{len(data_list)})'
    }
    return Response(response)
