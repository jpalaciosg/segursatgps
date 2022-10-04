from datetime import datetime,timedelta
from geopy.distance import great_circle
from shapely.geometry import Point,shape
import json

from users.models import Device
from locations.models import Location
from geofences.models import Geofence
from locations import serializers as locations_serializers

from common.time_conversor import TimeConversor
from common.device_reader import DeviceReader

time_conversor = TimeConversor()

class Report:

    def calculate_unit_ignition_events(self,unit,locations):
        ignition_events = []
        device_reader = DeviceReader(unit.uniqueid)
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(previous_location.attributes)
                })
                current_ignition = device_reader.detect_ignition_event({
                    'attributes':json.loads(current_location.attributes)
                })
                if previous_ignition == False and current_ignition == True:
                    #print('ON')
                    ignition_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'ON',
                    })
                elif previous_ignition == True and current_ignition == False:
                    #print('OFF')
                    ignition_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'OFF',
                    })
        return ignition_events

    def calculate_unit_movement_events(self,unit,locations):
        movement_events = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                if previous_location.speed == 0 and current_location.speed > 0:
                    #print('START')
                    movement_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'START',
                    })
                elif previous_location.speed > 0 and current_location.speed == 0:
                    #print('STOP')
                    movement_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'STOP',
                    })
        return movement_events

    def generate_detailed_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        device_reader = DeviceReader(unit.uniqueid)
        data = serializer.data
        for i in range(len(data)):
            data[i]['unit_name'] = unit.name
            data[i]['unit_description'] = unit.description
            data[i]['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                item['attributes'] = json.loads(item['attributes'])
            except:
                item['attributes'] = {}
            data[i]['ignition'] = device_reader.detect_ignition_event({
                'attributes':attributes
            })
            data[i]['odometer'] = device_reader.get_odometer({
                'attributes':attributes
            })
            if i == 0:
                data[i]['distance'] = 0.0
            else:
                distance = great_circle(
                    (
                        data[i-1]['latitude'],
                        data[i-1]['longitude']
                    ),
                    (
                        data[i]['latitude'],
                        data[i]['longitude']
                    ),
                ).km
                data[i]['distance'] = round(distance,2)
        return data

    def generate_driving_style_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        data = serializer.data

        harsh_driving_report = []
        harsh_braking = 0
        harsh_acceleration = 0
        harsh_cornering = 0
        device_reader = DeviceReader(unit.uniqueid)
        for i in range(len(data)):
            data[i]['unit_name'] = unit.name
            data[i]['unit_description'] = unit.description
            data[i]['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(data[i]['attributes'])
            except:
                attributes = []
            data[i]['attributes'] = attributes
            data[i]['ignition'] = device_reader.detect_ignition_event({
                'attributes':attributes
            })
            try:
                driving_incident = attributes['alarm']
                data[i]['driving'] = driving_incident
                data[i]['intensity'] = attributes['io254']
                if driving_incident == 'hardBraking': harsh_braking += 1
                if driving_incident == 'hardAcceleration': harsh_acceleration += 1
                if driving_incident == 'hardCornering': harsh_cornering += 1
                harsh_driving_report.append(data[i])
            except Exception as e:
                pass
        summarization = [
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'harshAcceleration',
            'amount': harsh_acceleration
            },
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'harshBraking',
            'amount': harsh_braking
            },
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'harshCornering',
            'amount': harsh_cornering
            },
        ]
        if len(harsh_driving_report) == 0:
            return {
                'harsh_driving_report':[],
                'summarization':[],
            }
        else:
            return {
                'harsh_driving_report':harsh_driving_report,
                'summarization':summarization,
            }

    def generate_speed_report(self,unit,initial_timestamp,final_timestamp,speed_limit):
        speed_report = []
        summarization = []
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        for item in serializer.data:
            if item['speed'] > speed_limit:
                item['unit_name'] = unit.name
                item['unit_description'] = unit.description
                item['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    item['timestamp'],"%d/%m/%Y %H:%M:%S")
                try:
                    item['attributes'] = json.loads(item['attributes'])
                except:
                    item['attributes'] = {}
                speed_report.append(item)
        summarization.append({
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'number_of_speeds': len(speed_report)
        })
        if len(speed_report) == 0: 
            return {
                'speed_report': [],
                'summarization': []
            }
        else:
            return {
                'speed_report': speed_report,
                'summarization': summarization
            }

    def generate_trip_report1(self,unit,initial_timestamp,final_timestamp,geofence_option):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lte=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        trip_report = []
        summarization = []
        ignition_events = self.calculate_unit_ignition_events(unit,locations)
        for i in range(len(ignition_events)):
            if i == 0:
                if ignition_events[i]['event'] == 'OFF':
                    trip_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':'N/D',
                        'initial_longitude':'N/D',
                        'initial_timestamp':'N/D',
                        'initial_datetime':'N/D',
                        'initial_address':'N/D',
                        'final_latitude':ignition_events[i]['latitude'],
                        'final_longitude':ignition_events[i]['longitude'],
                        'final_timestamp':ignition_events[i]['timestamp'],
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            ignition_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_address':ignition_events[i]['address'],
                        'trip_duration':'N/D',
                        'trip_time':'N/D',
                    })
                elif i == len(ignition_events)-1 and ignition_events[i]['event'] == 'ON':
                    trip_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':ignition_events[i]['latitude'],
                        'initial_longitude':ignition_events[i]['longitude'],
                        'initial_timestamp':ignition_events[i]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            ignition_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_address':ignition_events[i]['address'],
                        'final_latitude':'N/D',
                        'final_longitude':'N/D',
                        'final_timestamp':'N/D',
                        'final_datetime':'N/D',
                        'trip_duration':'N/D',
                        'trip_time':'N/D',
                    })
            else:
                if i == len(ignition_events)-1 and ignition_events[i]['event'] == 'ON':
                    trip_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':ignition_events[i]['latitude'],
                        'initial_longitude':ignition_events[i]['longitude'],
                        'initial_timestamp':ignition_events[i]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            ignition_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_address':ignition_events[i]['address'],
                        'final_latitude':'N/D',
                        'final_longitude':'N/D',
                        'final_timestamp':'N/D',
                        'final_datetime':'N/D',
                        'trip_duration':'N/D',
                        'trip_time':'N/D',
                    })
                elif ignition_events[i-1]['event'] == 'ON' and ignition_events[i]['event'] == 'OFF':
                    initial_datetime = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                        ignition_events[i-1]['timestamp'],"%d/%m/%Y %H:%M:%S")
                    final_datetime = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                        ignition_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
                    trip_duration = ignition_events[i]['timestamp'] - ignition_events[i-1]['timestamp']
                    trip_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':ignition_events[i-1]['latitude'],
                        'initial_longitude':ignition_events[i-1]['longitude'],
                        'initial_timestamp':ignition_events[i-1]['timestamp'],
                        'initial_datetime':initial_datetime,
                        'initial_address':ignition_events[i-1]['address'],
                        'final_latitude':ignition_events[i]['latitude'],
                        'final_longitude':ignition_events[i]['longitude'],
                        'final_timestamp':ignition_events[i]['timestamp'],
                        'final_datetime':final_datetime,
                        'final_address':ignition_events[i]['address'],
                        'trip_duration':trip_duration,
                        'trip_time':str(timedelta(seconds=trip_duration))
                    })
        for tr in trip_report:
            if tr['initial_timestamp'] == 'N/D' or tr['final_timestamp'] == 'N/D':
                tr['distance'] = 'N/D'
                tr['average_speed'] = 'N/D'
                tr['max_speed'] = 'N/D'
                tr['stop_duration'] = 'N/D'
                tr['stop_time'] = 'N/D'
                tr['driving_duration'] = 'N/D'
                tr['driving_time'] = 'N/D'
            else:
                trip_locations = locations.filter(
                    timestamp__gte=tr['initial_timestamp'],
                    timestamp__lte=tr['final_timestamp'],
                )
                distance = 0
                speeds = []
                for i in range(len(trip_locations)):
                    speeds.append(trip_locations[i].speed)
                    if i != 0:
                        previous_location = trip_locations[i-1]
                        current_location = trip_locations[i]
                        distance2 = great_circle(
                            (
                                previous_location.latitude,
                                previous_location.longitude,
                            ),
                            (
                                current_location.latitude,
                                current_location.longitude,
                            ),
                        ).km
                        distance += distance2
                tr['distance'] = round(distance,2)
                tr['average_speed'] = round(sum(speeds)/len(speeds),2)
                tr['max_speed'] = max(speeds)
                movement_events = self.calculate_unit_movement_events(unit,trip_locations)
                stop_duration = 0
                for i in range(len(movement_events)):
                    if i == 0:
                        if movement_events[i]['event'] == 'START':
                            stop_duration += movement_events[i]['timestamp'] - tr['initial_timestamp']
                        elif  i == len(movement_events)-1 and movement_events[i]['event'] == 'STOP':
                            stop_duration += tr['final_timestamp'] - movement_events[i]['timestamp']
                    else:
                        if i == len(movement_events)-1 and movement_events[i]['event'] == 'STOP':
                            stop_duration += tr['final_timestamp'] - movement_events[i]['timestamp']
                        elif movement_events[i-1]['event'] == 'STOP' and movement_events[i]['event'] == 'START':
                            stop_duration += movement_events[i]['timestamp'] - movement_events[i-1]['timestamp']
                tr['stop_duration'] = stop_duration
                tr['stop_time'] = str(timedelta(seconds=stop_duration))
                tr['driving_duration'] = tr['trip_duration'] - stop_duration
                tr['driving_time'] = str(timedelta(seconds=tr['driving_duration']))
        if geofence_option:
            geofences = Geofence.objects.filter(account=unit.account)
            for tr in trip_report:
                matching_initial_geofences = []
                matching_final_geofences = []
                for geofence in geofences:
                    feature = json.loads(geofence.geojson)['features'][0]
                    s = shape(feature['geometry'])
                    if tr['initial_longitude'] != 'N/D' and tr['initial_latitude'] != 'N/D':
                        initial_point = Point(tr['initial_longitude'],tr['initial_latitude'])
                        if s.contains(initial_point):
                            matching_initial_geofences.append(geofence.name)
                    if tr['final_longitude'] != 'N/D' and tr['final_latitude'] != 'N/D':
                        final_point = Point(tr['final_longitude'],tr['final_latitude'])
                        if s.contains(final_point):
                            matching_final_geofences.append(geofence.name)
                s_str = ""
                for i in range(len(matching_initial_geofences)):
                    if i==0:
                        s_str += matching_initial_geofences[i]
                    else:
                        s_str += f', {matching_initial_geofences[i]}'
                tr['initial_geofences'] = s_str
                d_str = ""
                for i in range(len(matching_final_geofences)):
                    if i==0:
                        d_str += matching_final_geofences[i]
                    else:
                        d_str += f', {matching_final_geofences[i]}'
                tr['final_geofences'] = d_str
        else:
            for tr in trip_report:
                tr['initial_geofences'] = 'N/D'
                tr['final_geofences'] = 'N/D'
        # CALCULAR RESUMEN
        number_of_trips = 0
        distance_summarization = 0.0
        trip_duration_summarization = 0
        stop_duration_summarization = 0
        for tr in trip_report:
            if tr['initial_timestamp'] != 'N/D':
                if tr['final_timestamp'] != 'N/D':
                    number_of_trips += 1
                    distance_summarization += tr['distance']
                    trip_duration_summarization += tr['trip_duration']
                    stop_duration_summarization += tr['stop_duration']
        driving_duration_summarization = trip_duration_summarization-stop_duration_summarization
        summarization.append({
            "unit_name" : unit.name,
            "unit_description": unit.description,
            "initial_datetime": time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            "final_datetime" : time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            "number_of_trips": number_of_trips,
            "distance_summarization": round(distance_summarization,2),
            "trip_duration_summarization": time_conversor.convert_seconds_in_hour_format(
                trip_duration_summarization),
            "stop_duration_summarization": time_conversor.convert_seconds_in_hour_format(
                stop_duration_summarization),
            "driving_duration_summarization": time_conversor.convert_seconds_in_hour_format(
                driving_duration_summarization),
        })
        # FIN - CALCULAR RESUMEN
        if len(trip_report) == 0: 
            return {
                'speed_report': [],
                'summarization': []
            }
        else:
            return {
                'trip_report': trip_report,
                'summarization': summarization,
            }