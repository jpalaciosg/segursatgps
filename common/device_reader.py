from datetime import datetime
from shapely.geometry import Point,shape
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

    def detect_battery_disconnection_event(self,current_location,previous_location):
        reader = Teltonika(self.deviceid)
        return reader.detect_battery_disconnection_event

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

    def generate_geofence_report(self,locations,geofences,initial_timestamp,final_timestamp):
        geofence_event_report = []
        geofence_report = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_point = Point(previous_location['longitude'],previous_location['latitude'])
                current_point = Point(current_location['longitude'],current_location['latitude'])
                for geofence in geofences:
                    feature = geofence.geojson['features'][0]
                    s = shape(feature['geometry'])
                    if s.contains(previous_point) == False and s.contains(current_point) == True:
                        geofence_event_report.append({
                            'name': geofence.name,
                            'timestamp': locations[i]['timestamp'],
                            'speed': locations[i]['speed'],
                            'event': 'INPUT'
                        })
                    elif s.contains(previous_point) == True and s.contains(current_point) == False:
                        geofence_event_report.append({
                            'name': geofence.name,
                            'timestamp': locations[i]['timestamp'],
                            'speed': locations[i]['speed'],
                            'event': 'OUTPUT'
                        })
        for i in range(len(geofence_event_report)):
            if i == 0:
                if geofence_event_report[i]['event'] == 'OUTPUT':
                    geofence_report.append({
                        'name': geofence_event_report[i]['name'],
                        'initial_timestamp': initial_timestamp,
                        'initial_speed': 'N/D',
                        'final_timestamp': geofence_event_report[i]['timestamp'],
                        'final_speed': geofence_event_report[i]['speed'],
                        'duration': geofence_event_report[i]['timestamp'] - initial_timestamp
                    })
            else:
                if i == len(geofence_event_report)-1 and geofence_event_report[i-1]['event'] == 'INPUT':
                    geofence_report.append({
                        'name': geofence_event_report[i]['name'],
                        'initial_timestamp': geofence_event_report[i]['timestamp'],
                        'initial_speed': geofence_event_report[i]['speed'],
                        'final_timestamp': final_timestamp,
                        'final_speed': 'N/D',
                        'duration': final_timestamp - geofence_event_report[i]['timestamp']
                    })
                else:
                    if geofence_event_report[i-1]['event'] == 'INPUT' and  geofence_event_report[i]['event'] == 'OUTPUT':
                        geofence_report.append({
                            'name': geofence_event_report[i]['name'],
                            'initial_timestamp': geofence_event_report[i-1]['timestamp'],
                            'initial_speed': geofence_event_report[i-1]['speed'],
                            'final_timestamp': geofence_event_report[i]['timestamp'],
                            'final_speed': geofence_event_report[i]['speed'],
                            'duration': geofence_event_report[i]['timestamp'] - geofence_event_report[i-1]['timestamp']
                        })
        return geofence_report