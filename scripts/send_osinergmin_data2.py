from units.models import Device
from datetime import datetime
import requests
import threading
import json

URL = 'https://prod.osinergmin-agent-2021.com/api/v1/trama'
TOKEN = '77616554-01CE-492A-AAB6-0A8E4273CAA8'

def thread_function(json_payload):
    global Device
    global requests
    global datetime
    global URL, TOKEN
    now = datetime.utcnow()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    headers = {
      'Content-Type': 'application/json; charset=utf-8',
    }
    response = requests.post(URL,headers=headers,data=json_payload)
    
    print('-----------------------------\n'+\
    f'Datetime: {dt_string}\n'+\
    'Payload:\n'+\
    f'{json_payload}\n'+\
    'Response:\n'+\
    response.text+'\n')

units = Device.objects.filter(osinergmin_process=True).order_by('id')
dt = datetime.utcnow()
dt_str = dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")
ts = int(datetime.timestamp(dt))

for unit in units:
    try:
        if unit.last_speed == 0:
            ts_offset = ts - unit.last_timestamp
            if ts_offset < 86400:
                item = {
                    "event": "none",
                    "plate": unit.name,
                    "speed": unit.last_speed,
                    "odometer": 0,
                    "position": {
                        "latitude": unit.last_latitude,
                        "longitude": unit.last_longitude,
                        "altitude": unit.last_altitude,
                    },
                    "gpsDate": dt_str,
                    "tokenTrama": TOKEN
                }
                item = json.dumps(item)
                #print(item)
                x = threading.Thread(target=thread_function, args=(item,))
                x.start()
    except Exception as e:
        print('ERROR:')
        print(e)