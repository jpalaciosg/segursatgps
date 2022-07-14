from locations.models import Location,SutranLocation,OsinergminLocation
from segursatgps.celery import celery_app

from datetime import datetime
import json
import redis

from common.device_reader import DeviceReader
from common.alert_reader import AlertReader
from common.gmt_conversor import GMTConversor
from common.repository import Repository

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
        location = Location.objects.create(
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
                #speed = data['speed'],
                speed = speed,
                event = event,
                device_datetime = device_datetime,
                #device_datetime = gmt_conversor.convert_utctolocaltime(datetime.utcnow()),
                server_datetime = gmt_conversor.convert_utctolocaltime(datetime.utcnow()),
            )
        except:
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
        except:
            print(e)   
    # FIN - INTRODUCIR UBICACION OSINERGMIN
    return True

@celery_app.task
def insert_location_in_history2(data):
    # INTRODUCIR UBICACION EN EL HISTORICO
    try:
        location = Location.objects.create(
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
    if battery_event:
        print('ALERTA BATERIA')
        device_datetime = datetime.fromtimestamp(data['current_location']['timestamp'])
        device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
        device_datetime_str = device_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        payload = {
            'group': data['current_location']['account'].upper(),
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
        print('ALERTA DE PANICO')
        device_datetime = datetime.fromtimestamp(data['current_location']['timestamp'])
        device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
        device_datetime_str = device_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        payload = {
            'group': data['current_location']['account'].upper(),
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