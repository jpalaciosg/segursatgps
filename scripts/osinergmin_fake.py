from units.models import Device

from datetime import datetime
import requests
import json
import time

URL = 'https://prod.osinergmin-agent-2021.com/api/v1/trama'
TOKEN = '77616554-01CE-492A-AAB6-0A8E4273CAA8'

unit_name = input("Ingresa la placa: ")
repetitions = int(input("Ingresa el numero de envios: "))

for i in range(repetitions):
    try:
        device = Device.objects.get(name=unit_name)
        dt = datetime.utcnow()
        dt_str = dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        item = {
            "event": "none",
            "plate": device.name,
            "speed": device.last_speed,
            "odometer": 0,
            "position": {
                "latitude": device.last_latitude,
                "longitude": device.last_longitude,
                "altitude": device.last_altitude
            },
            "gpsDate": dt_str,
            "tokenTrama": TOKEN
        }

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = requests.post(URL,headers=headers,data=json.dumps(item))
        print(item)
        print(response.text)
        print('----------------------------------')
        time.sleep(18)
    except Exception as e:
        print('ERROR:')
        print(e)