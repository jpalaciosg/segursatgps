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
            engine_hours = int(self.get_engine_hours({
                'attributes':data['last_attributes']
            }))
            engine_hours = int(engine_hours/1000)
            engine_hours = engine_hours % 60
            engine_seconds = engine_hours - engine_hours % 60
            data['engine_hours'] = f"{engine_hours} h {engine_seconds} s"
        except Exception as e:
            data['engine_hours'] = 'N/D'
        data['last_report'] = gmt_conversor.convert_utctolocaltime(
            datetime.fromtimestamp(unit.last_timestamp)
        )
        return data
	
    def generate_stop_report(self,locations,initial_timestamp,final_timestamp,seconds):
        reader = Teltonika(self.deviceid)
        return reader.generate_stop_report(locations,initial_timestamp,final_timestamp,seconds)

    def generate_trip_report(self,locations):
        reader = Teltonika(self.deviceid)
        return reader.generate_trip_report(locations)

    """
    def generate_driving_style_report(self,locations):
        reader = Teltonika(self.deviceid)
        return reader.generate_driving_style_report(locations)
    """

    def generate_speed_report(self,locations,speed_limit):
        speed_report = []
        for location in locations:
            if int(location['speed']) > speed_limit:
                speed_report.append({
                    'latitude':location['latitude'],
	                'longitude':location['longitude'],
	                'timestamp':location['timestamp'],
                    'altitude':location['altitude'],
                    'angle':location['angle'],
	                'speed':location['speed'],
	                'address':location['address'],
            })
        for sr in speed_report:
            sr['datetime'] = datetime.fromtimestamp(sr['timestamp'])
            sr['datetime'] = gmt_conversor.convert_utctolocaltime(sr['datetime']).strftime("%d/%m/%Y %H:%M:%S")
        return speed_report

    def generate_mileage_report(self,locations):
        distance_sum = 0.0
        for i in range(len(locations)):
            if i != 0:
                if locations[i-1]['latitude'] != 0.0 and locations[i-1]['longitude'] != 0.0:
                    if locations[i]['latitude'] != 0.0 and locations[i]['longitude'] != 0.0:
                        distance = great_circle(
                            (
                                locations[i-1]['latitude'],
                                locations[i-1]['longitude']
                            ),
                            (
                                locations[i]['latitude'],
                                locations[i]['longitude']
                            ),
                        ).km
                        distance_sum += distance
        return distance_sum

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
                    feature = json.loads(geofence.geojson)['features'][0]
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
                elif i == len(geofence_event_report)-1 and geofence_event_report[i]['event'] == 'INPUT':
                    geofence_report.append({
                        'name': geofence_event_report[i]['name'],
                        'initial_timestamp': geofence_event_report[i]['timestamp'],
                        'initial_speed': geofence_event_report[i]['speed'],
                        'final_timestamp': final_timestamp,
                        'final_speed': 'N/D',
                        'duration': final_timestamp - geofence_event_report[i]['timestamp']
                    })
            else:
                if i == len(geofence_event_report)-1 and geofence_event_report[i]['event'] == 'INPUT':
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
        for gr in geofence_report:
            gr['initial_datetime'] = datetime.fromtimestamp(gr['initial_timestamp'])
            gr['initial_datetime'] = gmt_conversor.convert_utctolocaltime(gr['initial_datetime']).strftime("%d/%m/%Y, %H:%M:%S")
            gr['final_datetime'] = datetime.fromtimestamp(gr['final_timestamp'])
            gr['final_datetime'] = gmt_conversor.convert_utctolocaltime(gr['final_datetime']).strftime("%d/%m/%Y, %H:%M:%S")
            gr['duration'] = str(timedelta(seconds=gr['duration']))
        return geofence_report