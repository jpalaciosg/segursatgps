from units.models import Device
from units.serializers import DeviceSerializer

from common.protocols.teltonika import Teltonika
from common.gmt_conversor import GMTConversor

from datetime import datetime,timedelta
from shapely.geometry import Point,shape
from geopy.distance import great_circle
import json

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

    def detect_battery_disconnection_event(self,current_location,previous_location):
        reader = Teltonika(self.deviceid)
        return reader.detect_battery_disconnection_event(current_location,previous_location)

    def detect_harsh_acceleration_event(self,location):
        reader = Teltonika(self.deviceid)
        return reader.detect_harsh_acceleration_event(location)

    def detect_harsh_braking_event(self,location):
        reader = Teltonika(self.deviceid)
        return reader.detect_harsh_braking_event(location)

    def detect_harsh_cornering_event(self,location):
        reader = Teltonika(self.deviceid)
        return reader.detect_harsh_cornering_event(location)

    def detect_valve1_event(self,unit,location):
        reader = Teltonika(self.deviceid)
        return reader.detect_valve1_event(unit,location)

    def detect_valve2_event(self,unit,location):
        reader = Teltonika(self.deviceid)
        return reader.detect_valve2_event(unit,location)

    def get_odometer(self,location):
        reader = Teltonika(self.deviceid)
        return reader.get_odometer(location)

    def get_hours(self,location):
        reader = Teltonika(self.deviceid)
        return reader.get_hours(location)

    def get_unit_status(self,unit):
        serializer = DeviceSerializer(unit,many=False)
        data = serializer.data
        try:
            data['last_attributes'] = json.loads(data['last_attributes'])
        except:
            data['last_attributes'] = ''
        try:
            c_time = int(self.get_hours({
                'attributes':data['last_attributes']
            }))
            hours = int(c_time/3600)
            minutes = int(c_time%3600/60)
            data['last_hours'] = f"{hours} h {minutes} m"
        except Exception as e:
            data['last_hours'] = 'N/D'
        try:
            temp = float(data['last_attributes']['temp1'])/0.1
            if int(temp) == 3000:
                data['temp'] = int(temp)
            else:
                data['temp'] = round(temp*0.001,2)
        except Exception as e:
            data['temp'] = 'N/D'
        data['last_report'] = gmt_conversor.convert_utctolocaltime(
            datetime.fromtimestamp(unit.last_timestamp)
        )
        return data
