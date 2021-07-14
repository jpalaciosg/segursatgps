from locations.models import Location,PanderoLocation,SutranLocation
from units.models import Device
from segursatgps.celery import celery_app

from datetime import datetime
import json

from common.alert_reader import AlertReader
from common.gmt_conversor import GMTConversor

gmt_conversor = GMTConversor() #conversor zona horaria

@celery_app.task
def insert_location_in_history(data):
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
    # INTRODUCIR UBICACION PANDERO LOCATION
    PANDERO_DEMO = ['BSJ-322','BSJ-627','BPY-670','BPY-669','BPY-636']
    if data['unit_name'] in PANDERO_DEMO:
        try:
            location2 = PanderoLocation.objects.create(
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
    # FIN - INTRODUCIR UBICACION PANDERO LOCATION
    # INTRODUCIR UBICACION SUTRAN
    if data['account'] == 'civa':
        try:
            if int(data['speed'] > 0): event = 'EN'
            else: event = 'PA'
            timestamp = data['timestamp']
            device_datetime = datetime.utcfromtimestamp(timestamp)
            device_datetime = gmt_conversor.convert_utctolocaltime(device_datetime)
            SutranLocation.objects.create(
                unit_name = data['unit_name'],
                latitude = data['latitude'],
                longitude = data['longitude'],
                angle = data['angle'],
                speed = data['speed'],
                event = event,
                device_datetime = device_datetime,
                server_datetime = gmt_conversor.convert_utctolocaltime(datetime.utcnow()),
            )
        except:
            print(e)   
    # FIN - INTRODUCIR UBICACION SUTRAN
    return True

@celery_app.task
def process_alert(data):
    alert_reader = AlertReader(data['deviceid'])
    alert_reader.run()
    del alert_reader
    return True