from locations.models import OsinergminLocation

from datetime import datetime
import requests
import threading
import json

URL = 'https://prod.osinergmin-agent-2021.com/api/v1/trama'
TOKEN = '77616554-01CE-492A-AAB6-0A8E4273CAA8'

def thread_function(json_payload,id):
    global OsinergminLocation
    global requests
    global datetime
    global URL, TOKEN
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    headers = {
      'Content-Type': 'application/json; charset=utf-8',
    }
    response = requests.post(URL,headers=headers,data=json_payload)
    location = OsinergminLocation.objects.get(id=id)
    location.it_was_sent = True
    location.save()
    print(f'Thread: {id}\n'+\
    '-----------------------------\n'+\
    f'Datetime: {dt_string}\n'+\
    'Payload:\n'+\
    f'{json_payload}\n'+\
    'Response:\n'+\
    response.text+'\n')

locations = OsinergminLocation.objects.using('history_db_replica').filter(it_was_sent=False).order_by('id')[:100]
print(len(locations))

for location in locations:
    try:
        #dt = datetime.utcfromtimestamp(location.timestamp)
        dt = datetime.utcnow()
        dt_str = dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        item = {
            "event": "none",
            "plate": location.reference,
            "speed": location.speed,
            "odometer": 0,
            "position": {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "altitude": location.altitude
            },
            "gpsDate": dt_str,
            "tokenTrama": TOKEN
        }
        item = json.dumps(item)
        print(item)
        x = threading.Thread(target=thread_function, args=(item,location.id,))
        x.start()
    except Exception as e:
        print('ERROR:')
        print(e)