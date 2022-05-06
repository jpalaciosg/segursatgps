from locations.models import Location
from units.models import Device

from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth 
import json

data = []
URL = 'http://190.12.73.86/json/json_receive.php'
#URL = 'http://190.12.73.86/json/rec27_segursat.php'
USER = ''
PASSWORD = ''

units = Device.objects.raw("SELECT * FROM units_device WHERE name IN ('D2K-714','T5F-888','V5T-883','V3L-822')")
print(len(units))

for unit in units:
    try:
        dt = datetime.fromtimestamp(unit.last_timestamp)
        dt = dt.strftime("%Y-%m-%dT%H:%M:%S")
        event = 2
        item = {
            "placa": unit.name,
            "latitud": str(unit.last_latitude),
            "longitud": str(unit.last_longitude),
            "direccion": unit.last_angle,
            "velocidad" : unit.last_speed,
            "evento" : str(event),
            "fechaEvento": dt.split('T')[0],
            "horaEvento": dt.split('T')[1],
        }
        print(item)
        data.append(item)
    except Exception as e:
        print('ERROR:')
        print(e)

data = {"items":data}
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
auth = HTTPBasicAuth(USER, PASSWORD)
headers = {
    'Content-Type': 'application/json; charset=utf-8',
}
response = requests.post(URL,headers=headers,data=json.dumps(data))
print(response.text)
