from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json
import channels.layers
from datetime import datetime,timedelta
from geopy.distance import great_circle
from asgiref.sync import async_to_sync

from .models import Location,SutranLocation
from units.models import Device
from .serializers import InsertLocationSerializer,LocationSerializer,InsertSutranLocationSerializer,InsertSolgasLocationSerializer
from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader
from common.privilege import Privilege
from .tasks import insert_location_in_history,insert_location_in_history2,process_alert,process_alert_without_notification,process_alerts_for_the_alert_center,process_location_in_background,process_thirdparty_location_in_background

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

@api_view(['POST'])
def insert_location_batch(request):
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
                ts = int(datetime.utcnow().timestamp())
                ts_offset = ts - data['timestamp']
                if ts_offset > 31536000:
                    data['timestamp'] = ts
                # FIN - CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
                # CAMBIAR VELOCIDAD SI ES MAYOR A 105 PARA CIVA
                if data['speed'] > 105 and unit.account.name=='civa':
                    data['speed'] = previous_location['speed']
                # FIN - CAMBIAR VELOCIDAD SI ES MAYOR A 105 PARA CIVA
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
                unit.previous_location = json.dumps(previous_location,ensure_ascii=False)
                # FIN CALCULAR UBICACION PREVIA
                # CALCULAR LAST_HOURS
                device_reader = DeviceReader(unit)
                hours = int(device_reader.get_hours({
                    'attributes':data['attributes']
                }))
                last_hours = int(device_reader.get_hours({
                    'attributes':attributes
                }))
                if hours > last_hours:
                    unit.last_hours = hours
                # FIN CALCULAR LAST_HOURS
                unit.last_address = data['address']
                if data['timestamp'] > previous_location['timestamp']:
                    unit.save()
                # INSERTAR UBICACION EN EL HISTORICO
                data['unit_id'] = unit.id
                data['unit_name'] = unit.name
                data['account'] = unit.account.name
                data['account_description'] = unit.account.name
                data['sutran_process'] = unit.sutran_process
                data['osinergmin_process'] = unit.osinergmin_process
                if data['timestamp'] != previous_location['timestamp']:
                    insert_location_in_history.delay(data)

                # ALERTAS
                process_alert.delay(data)
                # FIN - ALERTAS

                # ALERTAS CENTRAL
                process_alerts_for_the_alert_center.delay({
                    'uniqueid': unit.uniqueid,
                    'current_location': data,
                    'previous_location': previous_location,
                })
                # FIN - ALERTAS CENTRAL

                # ACTUALIZAR UNIDADES EN EL MAPA
                if data['timestamp'] > previous_location['timestamp']:
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
        else:
            errors = {
                'errors':serializer.errors
            }
            return Response(errors)
    if len(error_list) != 0:
        return Response(error_list)
    return Response([])

@api_view(['GET'])
def get_location_history(request,unitid,initial_datetime,final_datetime):
    initial_timestamp = None
    final_timestamp = None
    units = privilege.get_units(request)
    try:
        #unit = Device.objects.get(id=unitid)
        unit = [unit for unit in units if unit.id == unitid][0]
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
    locations = Location.objects.using('history_db_replica').filter(unitid=unit.id,timestamp__gte=initial_timestamp,timestamp__lte=final_timestamp).order_by('timestamp')
    serializer = LocationSerializer(locations,many=True)
    data = serializer.data
    data1 = []
    for i in range(len(data)):
        if data[i]['latitude'] != 0.0 and data[i]['longitude'] != 0.0:
            data[i]['unit_name'] = unit.name
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
