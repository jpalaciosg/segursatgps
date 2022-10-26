from django.conf import settings

from locations.models import Location,SutranLocation,OsinergminLocation
from units.models import Device
from geofences.models import Geofence
from users.models import Account
from segursatgps.celery import celery_app

from common.device_reader import DeviceReader
from common.alert_reader import AlertReader
from common.gmt_conversor import GMTConversor
from common.repository import Repository

from datetime import datetime
from geopy.distance import great_circle
from asgiref.sync import async_to_sync
from shapely.geometry import Point,shape
import channels.layers
import json
import redis
import requests

gmt_conversor = GMTConversor() #conversor zona horaria
repository = Repository()

@celery_app.task
def insert_location_in_history(data):
    # INTRODUCIR UBICACION EN EL HISTORICO
    """
    try:
        repository.write(data)
    except Exception as e:
        print(e)
    """
    try:
        Location.objects.create(
            unitid = data['unit_id'],
            protocol= data['protocol'],
            timestamp = data['timestamp'],
            latitude = data['latitude'],
            longitude = data['longitude'],
            altitude = data['altitude'],
            angle = data['angle'],
            speed = data['speed'],
            attributes = json.dumps(data['attributes']),
            address = data['address'],
            reference = data['unit_name']
        )
    except Exception as e:
        print(e)
    # FIN - INTRODUCIR UBICACION EN EL HISTORICO
    # INTRODUCIR UBICACION SUTRAN
    if data['account'] == 'civa' or data['account'] == 'alcas' or data['account'] == 'miskymayo' or data['sutran_process']:
        try:
            event = 'EN' if int(data['speed'] > 0) else 'PA'
            timestamp = data['timestamp']
            device_datetime = datetime.utcfromtimestamp(timestamp)
            device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
            speed = 95 if int(data['speed']) > 95 else data['speed']
            SutranLocation.objects.create(
                unit_name = data['unit_name'],
                latitude = data['latitude'],
                longitude = data['longitude'],
                angle = data['angle'],
                speed = speed,
                event = event,
                device_datetime = device_datetime,
                server_datetime = gmt_conversor.convert_utctolocaltime(datetime.utcnow()),
            )
        except Exception as e:
            print(e)
    # FIN - INTRODUCIR UBICACION SUTRAN
    # INTRODUCIR UBICACION OSINERGMIN
    if data['osinergmin_process']:
        try:
            OsinergminLocation.objects.create(
                unitid = data['unit_id'],
                protocol= data['protocol'],
                timestamp = data['timestamp'],
                latitude = data['latitude'],
                longitude = data['longitude'],
                altitude = data['altitude'],
                angle = data['angle'],
                speed = data['speed'],
                attributes = json.dumps(data['attributes']),
                address = data['address'],
                reference = data['unit_name']
            )
        except Exception as e:
            print(e)   
    # FIN - INTRODUCIR UBICACION OSINERGMIN
    return True

@celery_app.task
def insert_location_in_history2(data):
    # INTRODUCIR UBICACION EN EL HISTORICO
    try:
        Location.objects.create(
            unitid = data['unit_id'],
            protocol= data['protocol'],
            timestamp = data['timestamp'],
            latitude = data['latitude'],
            longitude = data['longitude'],
            altitude = data['altitude'],
            angle = data['angle'],
            speed = data['speed'],
            attributes = json.dumps(data['attributes']),
            address = data['address'],
            reference = data['unit_name']
        )
    except Exception as e:
        print(e)
    # FIN - INTRODUCIR UBICACION EN EL HISTORICO
    return True

@celery_app.task
def process_alert(data):
    alert_reader = AlertReader(data['deviceid'])
    alert_reader.run()
    del alert_reader
    return True

@celery_app.task
def process_history_alert(data):
    alert_reader = AlertReader(data['deviceid'])
    alert_reader.run()
    del alert_reader
    return True

@celery_app.task
def process_alerts_for_the_alert_center(data):
    device_reader = DeviceReader(data['uniqueid'])
    panic_event = device_reader.detect_panic_event(data['current_location'])
    battery_event = device_reader.detect_battery_disconnection_event(data['current_location'],data['previous_location'])
    geofence_exit_event = False
    if data['current_location']['account'] == '20603017847':
        try:
            account = Account.objects.get(name='20603017847') # cuenta hng_inversiones
            geofence = Geofence.objects.get(name='ZONA AUTORIZADA LIMA',account=account)
            geojson = json.loads(geofence.geojson)
            s = shape(geojson['features'][0]['geometry'])
            point1 = Point(data['current_location']['longitude'],data['current_location']['latitude'])
            point2 = Point(data['previous_location']['longitude'],data['previous_location']['latitude'])
            if s.contains(point2) == True and s.contains(point1) == False:
                geofence_exit_event = True
        except Exception as e:
            pass
    if battery_event:
        device_datetime = datetime.fromtimestamp(data['current_location']['timestamp'])
        device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
        device_datetime_str = device_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        payload = {
            #'group': data['current_location']['account'].upper(),
            'group': data['current_location']['account_description'].upper(),
            'license_plate': data['current_location']['unit_name'],
            'device_datetime': device_datetime_str,
            'latitude': data['current_location']['latitude'],
            'longitude': data['current_location']['longitude'],
            'speed': data['current_location']['speed'],
            'angle': data['current_location']['angle'],
            'alert_type': "ALERTA DE BATERIA - NP"
        }
        redis_client = redis.StrictRedis(host='localhost',port=6379,db=0)
        redis_client.rpush('ssatAlertQueue', json.dumps(payload))
    if panic_event:
        device_datetime = datetime.fromtimestamp(data['current_location']['timestamp'])
        device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
        device_datetime_str = device_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        payload = {
            #'group': data['current_location']['account'].upper(),
            'group': data['current_location']['account_description'].upper(),
            'license_plate': data['current_location']['unit_name'],
            'device_datetime': device_datetime_str,
            'latitude': data['current_location']['latitude'],
            'longitude': data['current_location']['longitude'],
            'speed': data['current_location']['speed'],
            'angle': data['current_location']['angle'],
            'alert_type': "ALERTA DE PANICO - NP"
        }
        redis_client = redis.StrictRedis(host='localhost',port=6379,db=0)
        redis_client.rpush('ssatAlertQueue', json.dumps(payload))
    if geofence_exit_event:
        device_datetime = datetime.fromtimestamp(data['current_location']['timestamp'])
        device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
        device_datetime_str = device_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        payload = {
            'group': data['current_location']['account_description'].upper(),
            'license_plate': data['current_location']['unit_name'],
            'device_datetime': device_datetime_str,
            'latitude': data['current_location']['latitude'],
            'longitude': data['current_location']['longitude'],
            'speed': data['current_location']['speed'],
            'angle': data['current_location']['angle'],
            'alert_type': "ALERTA DE SALIDA DE GEOCERCA HNG_INVERSIONES - NP"
        }
        redis_client = redis.StrictRedis(host='localhost',port=6379,db=0)
        redis_client.rpush('ssatAlertQueue', json.dumps(payload))
    return True

@celery_app.task
def process_location_in_background(data):
    unit = None
    try:
        deviceid = data['deviceid']
        unit = Device.objects.get(uniqueid=deviceid)
    except Exception as e:
        pass
    if unit:
        try:
            previous_attributes = json.loads(unit.last_attributes)
        except Exception as e:
            previous_attributes = json.loads("{}")
        previous_location = {
            'timestamp':unit.last_timestamp,
            'latitude':unit.last_latitude,
            'longitude':unit.last_longitude,
            'altitude':unit.last_altitude,
            'angle':unit.last_angle,
            'speed':unit.last_speed,
            'attributes':previous_attributes,
            'address':unit.last_address
        }
        # CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
        ts = int(datetime.utcnow().timestamp())
        ts_offset = ts - data['timestamp']
        if ts_offset > 31536000:
            data['timestamp'] = ts
        # FIN - CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
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
        # FIN - CALCULAR UBICACION PREVIA
        # CALCULAR LAST_HOURS
        device_reader = DeviceReader(unit.uniqueid)
        hours = int(device_reader.get_hours({
            'attributes':data['attributes']
        }))
        last_hours = int(device_reader.get_hours({
            'attributes':previous_attributes
        }))
        if hours > last_hours:
            unit.last_hours = hours
        # FIN - CALCULAR LAST_HOURS
        # CALCULAR DIRECCION ULTIMA POSICION
        if data['address'] == "":
            try:
                latitude = float(data['latitude'])
                longitude = float(data['longitude'])
                api_url = f'http://{settings.GEOCODING_SERVER}/nominatim/reverse?format=jsonv2&lat={latitude}&lon={longitude}&addressdetails=1'
                headers = {'Content-Type': 'application/json'}
                response = requests.get(api_url,headers=headers,timeout=settings.GEOCODING_TIMEOUT)
                address = json.loads(response.content.decode('utf-8'))['display_name']
                #address = json.dumps(address,ensure_ascii=False)
            except Exception as e:
                print(e)
                address = ""
            data['address'] = address
        # FIN - CALCULAR DIRECCION ULTIMA POSICION
        unit.last_address = data['address']
        if data['timestamp'] > previous_location['timestamp']:
            unit.save()
        # ACTUALIZAR UNIDAD EN EL MAPA
        if data['timestamp'] > previous_location['timestamp']:
            account_name = unit.account.name
            last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data['timestamp']))
            last_report = last_report.strftime("%d/%m/%Y, %H:%M:%S")
            channel_layer = channels.layers.get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'chat_{account_name}',
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
        # FIN - ACTUALIZAR UNIDAD EN EL MAPA
        # INSERTAR UBICACION EN EL HISTORICO
        data['unit_id'] = unit.id
        data['unit_name'] = unit.name
        """
        try:
            repository.write(data)
        except Exception as e:
            print(e)
        """
        try:
            Location.objects.create(
                unitid = data['unit_id'],
                protocol= data['protocol'],
                timestamp = data['timestamp'],
                latitude = data['latitude'],
                longitude = data['longitude'],
                altitude = data['altitude'],
                angle = data['angle'],
                speed = data['speed'],
                attributes = json.dumps(data['attributes']),
                address = data['address'],
                reference = data['unit_name']
            )
        except Exception as e:
            print(e)
        # FIN - INSERTAR UBICACION EN EL HISTORICO
        # INSERTAR EN LA TABLA SUTRAN
        if unit.sutran_process:
            try:
                event = 'EN' if int(data['speed'] > 0) else 'PA'
                timestamp = data['timestamp']
                device_datetime = datetime.utcfromtimestamp(timestamp)
                device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
                speed = 95 if int(data['speed']) > 95 else data['speed']
                SutranLocation.objects.create(
                    unit_name = unit.name,
                    latitude = data['latitude'],
                    longitude = data['longitude'],
                    angle = data['angle'],
                    speed = speed,
                    event = event,
                    device_datetime = device_datetime,
                    server_datetime = gmt_conversor.convert_utctolocaltime(datetime.utcnow()),
                )
            except Exception as e:
                print(f"ERROR SUTRAN: {str(e)}")
        # FIN - INSERTAR EN LA TABLA SUTRAN
        # DETECTAR ALERTAS
        alert_reader = AlertReader(data['deviceid'])
        alert_reader.run()
        # FIN - DETECTAR ALERTAS
    return True

@celery_app.task
def process_thirdparty_location_in_background(data):
    unit = None
    try:
        deviceid = data['deviceid']
        unit = Device.objects.get(
            uniqueid = deviceid,
            is_replica = True
        )
    except Exception as e:
        pass
    if unit:
        try:
            previous_attributes = json.loads(unit.last_attributes)
        except Exception as e:
            previous_attributes = json.loads("{}")
        previous_location = {
            'timestamp':unit.last_timestamp,
            'latitude':unit.last_latitude,
            'longitude':unit.last_longitude,
            'altitude':unit.last_altitude,
            'angle':unit.last_angle,
            'speed':unit.last_speed,
            'attributes':previous_attributes,
            'address':unit.last_address
        }
        # CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
        ts = int(datetime.utcnow().timestamp())
        ts_offset = ts - data['timestamp']
        if ts_offset > 31536000:
            data['timestamp'] = ts
        # FIN - CAMBIAR TIMESTAMP SI TIENE MAS DE 1 AÑO DE ANTIGUEDAD
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
        # FIN - CALCULAR UBICACION PREVIA
        # CALCULAR LAST_HOURS
        device_reader = DeviceReader(unit.uniqueid)
        hours = int(device_reader.get_hours({
            'attributes':data['attributes']
        }))
        last_hours = int(device_reader.get_hours({
            'attributes':previous_attributes
        }))
        if hours > last_hours:
            unit.last_hours = hours
        # FIN - CALCULAR LAST_HOURS
        # CALCULAR DIRECCION ULTIMA POSICION
        if data['address'] == "":
            try:
                latitude = float(data['latitude'])
                longitude = float(data['longitude'])
                api_url = f'http://{settings.GEOCODING_SERVER}/nominatim/reverse?format=jsonv2&lat={latitude}&lon={longitude}&addressdetails=1'
                headers = {'Content-Type': 'application/json'}
                response = requests.get(api_url,headers=headers,timeout=settings.GEOCODING_TIMEOUT)
                address = json.loads(response.content.decode('utf-8'))['display_name']
                #address = json.dumps(address,ensure_ascii=False)
            except Exception as e:
                print(e)
                address = ""
            data['address'] = address
        # FIN - CALCULAR DIRECCION ULTIMA POSICION
        unit.last_address = data['address']
        if data['timestamp'] > previous_location['timestamp']:
            unit.save()
        # ACTUALIZAR UNIDAD EN EL MAPA
        if data['timestamp'] > previous_location['timestamp']:
            account_name = unit.account.name
            last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data['timestamp']))
            last_report = last_report.strftime("%d/%m/%Y, %H:%M:%S")
            channel_layer = channels.layers.get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'chat_{account_name}',
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
        # FIN - ACTUALIZAR UNIDAD EN EL MAPA
        # INSERTAR UBICACION EN EL HISTORICO
        data['unit_id'] = unit.id
        data['unit_name'] = unit.name
        try:
            Location.objects.create(
                unitid = data['unit_id'],
                protocol= data['protocol'],
                timestamp = data['timestamp'],
                latitude = data['latitude'],
                longitude = data['longitude'],
                altitude = data['altitude'],
                angle = data['angle'],
                speed = data['speed'],
                attributes = json.dumps(data['attributes']),
                address = data['address'],
                reference = data['unit_name']
            )
        except Exception as e:
            print(e)
        # FIN - INSERTAR UBICACION EN EL HISTORICO
        # DETECTAR ALERTAS
        alert_reader = AlertReader(data['deviceid'])
        alert_reader.run()
        # FIN - DETECTAR ALERTAS
    return True