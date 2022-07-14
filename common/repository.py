from pathlib import Path
from datetime import datetime
import json

class Repository:
    def write(self,data):
        payload = {
            'unitid': data['unit_id'],
            'protocol': data['protocol'],
            'timestamp': data['timestamp'],
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'altitude': data['altitude'],
            'angle': data['angle'],
            'speed': data['speed'],
            'attributes': data['attributes'],
            'address': data['address'],
            'reference': data['unit_name']
        }
        payload = json.dumps(payload,ensure_ascii=False)
        payload = payload+'\n'
        #payload = ' '.join(format(x,'b') for x in bytearray(payload,'utf-8'))
        date_str = datetime.utcfromtimestamp(data['timestamp']).strftime("%Y%m%d")
        path = Path(f"/repository/{date_str}/{data['unit_id']}")
        path.parent.mkdir(exist_ok=True, parents=True)
        f = path.open("ab")
        f.write(payload.encode())
        f.close()