from datetime import datetime
import json

from units.models import Device
from units.serializers import DeviceSerializer

from common.protocols.teltonika import Teltonika
from common.gmt_conversor import GMTConversor

gmt_conversor = GMTConversor()

class DeviceReader:
    def __init__(self, deviceid):
        self.deviceid = deviceid

    def detect_ignition_event(self,location):
	    reader = Teltonika(self.deviceid)
	    return reader.detect_ignition_event(location)

    def detect_panic_event(self,location):
	    reader = Teltonika(self.deviceid)
	    return reader.detect_panic_event(location)
	
    def generate_stop_report(self,locations,initial_timestamp,final_timestamp):
	    reader = Teltonika(self.deviceid)
	    return reader.generate_stop_report(locations,initial_timestamp,final_timestamp)

    def generate_travel_report(self,locations):
	    reader = Teltonika(self.deviceid)
	    return reader.generate_travel_report(locations)

    def generate_speed_report(self,locations,speed_limit):
        speed_report = []
        for location in locations:
            if int(location['speed']) > speed_limit:
                speed_report.append({
                    'latitude':location['latitude'],
	                'longitude':location['longitude'],
	                'timestamp':location['timestamp'],
                    'angle':location['angle'],
	                'speed':location['speed'],
	                'address':location['address'],
            })
        for sr in speed_report:
            sr['dt'] = datetime.fromtimestamp(sr['timestamp'])
            sr['dt'] = gmt_conversor.convert_utctolocaltime(sr['dt']).strftime("%d/%m/%Y, %H:%M:%S")
        return speed_report

    def get_unit_status(self,unit):
        serializer = DeviceSerializer(unit,many=False)
        data = serializer.data
        try:
            data['last_attributes'] = json.loads(data['last_attributes'])
        except:
            data['last_attributes'] = ''
        data['last_report'] = gmt_conversor.convert_utctolocaltime(
            datetime.fromtimestamp(unit.last_timestamp)
        )
        return data