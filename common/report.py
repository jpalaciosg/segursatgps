from datetime import datetime,timedelta
from geopy.distance import great_circle
from shapely.geometry import Point,shape
from statistics import mean,median
from functools import reduce
from statistics import mean
import json

from locations.models import Location
from geofences.models import Geofence
from locations import serializers as locations_serializers

from common.gmt_conversor import GMTConversor
from common.time_conversor import TimeConversor
from common.device_reader import DeviceReader
from common.position_store import PositionStore

gmt_conversor = GMTConversor()
time_conversor = TimeConversor()
position_store = PositionStore()

class Report:

    def calculate_unit_ignition_events(self,unit,locations):
        ignition_events = []
        device_reader = DeviceReader(unit)
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
                        'id':locations[i].id,
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'START',
                    })
                elif previous_location.speed > 0 and current_location.speed == 0:
                    #print('STOP')
                    movement_events.append({
                        'id':locations[i].id,
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'STOP',
                    })
        return movement_events

    def calculate_unit_speed_events(self,unit,locations,speed_limit):
        speed_events = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                if previous_location.speed <= speed_limit and current_location.speed > speed_limit:
                    #print('START')
                    speed_events.append({
                        'id':locations[i].id,
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'speed':locations[i].speed,
                        'address':locations[i].address,
                        'event':'SPEED_START',
                    })
                elif previous_location.speed > speed_limit and current_location.speed <= speed_limit:
                    #print('STOP')
                    speed_events.append({
                        'id':locations[i].id,
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'speed':locations[i].speed,
                        'address':locations[i].address,
                        'event':'SPEED_STOP',
                    })
        return speed_events

    def calculate_long_speed_report(self,unit,initial_timestamp,final_timestamp,speed_limit,locations):
        speed_report = []
        summarization = []
        speed_events = self.calculate_unit_speed_events(unit,locations,speed_limit)
        for i in range(len(speed_events)):
            if i == 0:
                if speed_events[i]['event'] == 'SPEED_STOP':
                    speed_duration = speed_events[i]['timestamp'] - initial_timestamp
                    positions = ([
                        {'latitude':location.latitude,'longitude':location.longitude,'timestamp':location.timestamp,'speed':location.speed,'address':location.address}
                        for location in locations
                        if
                            location.timestamp >= initial_timestamp and
                            location.timestamp < speed_events[i]['timestamp']
                    ])
                    distance = sum([
                        great_circle(
                            (positions[i-1]['latitude'],positions[i-1]['longitude']),
                            (positions[i]['latitude'],positions[i]['longitude']),
                        ).km
                        for i in range(len(positions))
                            if i != 0
                    ])
                    trespass_level = 'MILD' if speed_duration<10 and distance<8 else 'MODERATE' if speed_duration<10 and distance<14 else 'SEVERE'
                    speeds = [ position['speed'] for position in positions ]
                    speed_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':'N/D',
                        'initial_longitude':'N/D',
                        'initial_timestamp':initial_timestamp,
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'initial_address':'N/D',
                        'final_latitude':speed_events[i]['latitude'],
                        'final_longitude':speed_events[i]['longitude'],
                        'final_timestamp':speed_events[i]['timestamp'],
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            speed_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_address':speed_events[i]['address'],
                        'speed_duration':speed_duration,
                        'speed_time':str(timedelta(seconds=speed_duration)),
                        'positions':positions,
                        'distance':round(distance,2),
                        'mean_speed':round(mean(speeds),2),
                        'max_speed':max(speeds),
                        'trespass_level':trespass_level,
                    })
                elif i == len(speed_events)-1 and speed_events[i]['event'] == 'SPEED_START':
                    speed_duration =  final_timestamp - speed_events[i]['timestamp']
                    positions = ([
                        {'latitude':location.latitude,'longitude':location.longitude,'timestamp':location.timestamp,'speed':location.speed,'address':location.address}
                        for location in locations
                            if
                            location.timestamp >= speed_events[i]['timestamp'] and
                            location.timestamp < final_timestamp
                    ])
                    distance = sum([
                        great_circle(
                            (positions[i-1]['latitude'],positions[i-1]['longitude']),
                            (positions[i]['latitude'],positions[i]['longitude']),
                        ).km
                        for i in range(len(positions))
                            if i != 0
                    ])
                    trespass_level = 'MILD' if speed_duration<10 and distance<8 else 'MODERATE' if speed_duration<10 and distance<14 else 'SEVERE'
                    speeds = [ position['speed'] for position in positions ]
                    speed_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':speed_events[i]['latitude'],
                        'initial_longitude':speed_events[i]['longitude'],
                        'initial_timestamp':speed_events[i]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            speed_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_address':speed_events[i]['address'],
                        'final_latitude':'N/D',
                        'final_longitude':'N/D',
                        'final_timestamp':final_timestamp,
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'final_address':'N/D',
                        'speed_duration':speed_duration,
                        'speed_time':str(timedelta(seconds=speed_duration)),
                        'positions':positions,
                        'distance':round(distance,2),
                        'mean_speed':round(mean(speeds),2),
                        'max_speed':max(speeds),
                        'trespass_level':trespass_level,
                    })
            else:
                if i == len(speed_events)-1 and speed_events[i]['event'] == 'SPEED_START':
                    speed_duration =  final_timestamp - speed_events[i]['timestamp']
                    positions = ([
                        {'latitude':location.latitude,'longitude':location.longitude,'timestamp':location.timestamp,'speed':location.speed,'address':location.address}
                        for location in locations
                            if
                            location.timestamp >= speed_events[i]['timestamp'] and
                            location.timestamp < final_timestamp
                    ])
                    distance = sum([
                        great_circle(
                            (positions[i-1]['latitude'],positions[i-1]['longitude']),
                            (positions[i]['latitude'],positions[i]['longitude']),
                        ).km
                        for i in range(len(positions))
                            if i != 0
                    ])
                    trespass_level = 'MILD' if speed_duration<10 and distance<8 else 'MODERATE' if speed_duration<10 and distance<14 else 'SEVERE'
                    speeds = [ position['speed'] for position in positions ]
                    speed_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':speed_events[i]['latitude'],
                        'final_longitude':speed_events[i]['longitude'],
                        'initial_timestamp':speed_events[i]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            speed_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_address':speed_events[i]['address'],
                        'final_latitude':'N/D',
                        'final_longitude':'N/D',
                        'final_timestamp':final_timestamp,
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'final_address':'N/D',
                        'speed_duration':speed_duration,
                        'speed_time':str(timedelta(seconds=speed_duration)),
                        'positions':positions,
                        'distance':round(distance,2),
                        'mean_speed':round(mean(speeds),2),
                        'max_speed':max(speeds),
                        'trespass_level':trespass_level,
                    })
                elif speed_events[i-1]['event'] == 'SPEED_START' and speed_events[i]['event'] == 'SPEED_STOP':
                    speed_duration = speed_events[i]['timestamp'] - speed_events[i-1]['timestamp']
                    positions = ([
                        {'latitude':location.latitude,'longitude':location.longitude,'timestamp':location.timestamp,'speed':location.speed,'address':location.address}
                        for location in locations
                            if
                            location.timestamp >= speed_events[i-1]['timestamp'] and
                            location.timestamp < speed_events[i]['timestamp']
                    ])
                    distance = sum([
                        great_circle(
                            (positions[i-1]['latitude'],positions[i-1]['longitude']),
                            (positions[i]['latitude'],positions[i]['longitude']),
                        ).km
                        for i in range(len(positions))
                            if i != 0
                    ])
                    trespass_level = 'MILD' if speed_duration<10 and distance<8 else 'MODERATE' if speed_duration<10 and distance<14 else 'SEVERE'
                    speeds = [ position['speed'] for position in positions ]
                    speed_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'initial_latitude':speed_events[i-1]['latitude'],
                        'initial_longitude':speed_events[i-1]['longitude'],
                        'initial_timestamp':speed_events[i-1]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            speed_events[i-1]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_address':speed_events[i-1]['address'],
                        'final_latitude':speed_events[i]['latitude'],
                        'final_longitude':speed_events[i]['longitude'],
                        'final_timestamp':speed_events[i]['timestamp'],
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            speed_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_address':speed_events[i]['address'],
                        'speed_duration':speed_duration,
                        'speed_time':str(timedelta(seconds=speed_duration)),
                        'positions':positions,
                        'distance':round(distance,2),
                        'mean_speed':round(mean(speeds),2),
                        'max_speed':max(speeds),
                        'trespass_level':trespass_level,
                    })
        # LIMPIAR ITEMS CON SOLO UNA VELOCIDAD
        speed_report = [ sr for sr in speed_report if len(sr['positions']) > 1 ]
        # fin - LIMPIAR ITEMS CON SOLO UNA VELOCIDAD
        if len(speed_report) > 0:
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                'number_of_speeds': len(speed_report),
            })
        return {
            'speed_report': speed_report,
            'summarization': summarization
        }

    """
    def generate_detailed_report(self,unit,initial_timestamp,final_timestamp):
        device_reader = DeviceReader(unit)
        data = position_store.read(unit.id,unit.account.id,initial_timestamp,final_timestamp)
        detailed_report = []
        for i in range(len(data)):
            dt = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(data[i]['attributes'])
            except:
                attributes = {}
            ignition = device_reader.detect_ignition_event({
                'attributes':attributes
            })
            odometer = device_reader.get_odometer({
                'attributes':attributes
            })
            detailed_report.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': dt,
                'latitude': data[i]['latitude'],
                'longitude': data[i]['longitude'],
                'altitude': data[i]['altitude'],
                'angle': data[i]['angle'],
                'speed': data[i]['speed'],
                'odometer': odometer,
                'ignition': ignition,
                'address': data[i]['address'],
            })
        return detailed_report
    """
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
        device_reader = DeviceReader(unit)
        data = serializer.data
        for i in range(len(data)):
            data[i]['unit_name'] = unit.name
            data[i]['unit_description'] = unit.description
            data[i]['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(data[i]['attributes'])
            except:
                attributes = {}
            data[i]['attributes'] = attributes
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

    def generate_extended_detailed_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        device_reader = DeviceReader(unit)
        data = serializer.data
        valve1_counter = 0
        valve2_counter = 0
        for i in range(len(data)):
            data[i]['unit_name'] = unit.name
            data[i]['unit_description'] = unit.description
            data[i]['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(data[i]['attributes'])
            except:
                attributes = {}
            data[i]['attributes'] = attributes
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
        
        # CALCULAR EVENTOS
        valve1_events = []
        valve2_events = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_valve1 = device_reader.detect_valve1_event({
                    'attributes':json.loads(previous_location.attributes)
                })
                current_valve1 = device_reader.detect_valve1_event({
                    'attributes':json.loads(current_location.attributes)
                })
                if previous_valve1 == False and current_valve1 == True:
                    #print('ON')
                    valve1_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'OPEN',
                    })
                elif previous_valve1 == True and current_valve1 == False:
                    #print('OFF')
                    valve1_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'CLOSE',
                    })
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_valve2 = device_reader.detect_valve2_event({
                    'attributes':json.loads(previous_location.attributes)
                })
                current_valve2 = device_reader.detect_valve2_event({
                    'attributes':json.loads(current_location.attributes)
                })
                if previous_valve2 == False and current_valve2 == True:
                    #print('ON')
                    valve2_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'OPEN',
                    })
                elif previous_valve2 == True and current_valve2 == False:
                    #print('OFF')
                    valve2_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'CLOSE',
                    })
        # FIN - CALCULAR EVENTOS

        summarization = [
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'valve1',
            'amount': len(valve1_events),
            },
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'valve2',
            'amount': len(valve2_events),
            },
        ]
        if len(data) == 0:
            return {
                'valve_report':[],
                'events':{
                    'valve1_events':[],
                    'valve2_events':[],
                },
                'summarization':[],
            }
        else:
            return {
                'valve_report':data,
                'events':{
                    'valve1_events':valve1_events,
                    'valve2_events':valve2_events,
                },
                'summarization':summarization,
            }

    def generate_extended_detailed_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        device_reader = DeviceReader(unit)
        data = serializer.data
        valve1_counter = 0
        valve2_counter = 0
        for i in range(len(data)):
            data[i]['unit_name'] = unit.name
            data[i]['unit_description'] = unit.description
            data[i]['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(data[i]['attributes'])
            except:
                attributes = {}
            data[i]['attributes'] = attributes
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
        
        # CALCULAR EVENTOS
        valve1_events = []
        valve2_events = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_valve1 = device_reader.detect_valve1_event({
                    'attributes':json.loads(previous_location.attributes)
                })
                current_valve1 = device_reader.detect_valve1_event({
                    'attributes':json.loads(current_location.attributes)
                })
                if previous_valve1 == False and current_valve1 == True:
                    #print('ON')
                    valve1_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'OPEN',
                    })
                elif previous_valve1 == True and current_valve1 == False:
                    #print('OFF')
                    valve1_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'CLOSE',
                    })
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_valve2 = device_reader.detect_valve2_event({
                    'attributes':json.loads(previous_location.attributes)
                })
                current_valve2 = device_reader.detect_valve2_event({
                    'attributes':json.loads(current_location.attributes)
                })
                if previous_valve2 == False and current_valve2 == True:
                    #print('ON')
                    valve2_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'OPEN',
                    })
                elif previous_valve2 == True and current_valve2 == False:
                    #print('OFF')
                    valve2_events.append({
                        'latitude':locations[i].latitude,
                        'longitude':locations[i].longitude,
                        'timestamp':locations[i].timestamp,
                        'address':locations[i].address,
                        'event':'CLOSE',
                    })
        # FIN - CALCULAR EVENTOS

        summarization = [
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'valve1',
            'amount': len(valve1_events),
            },
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                initial_timestamp,"%d/%m/%Y %H:%M:%S"),
            'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                final_timestamp,"%d/%m/%Y %H:%M:%S"),
            'type': 'valve2',
            'amount': len(valve2_events),
            },
        ]
        if len(data) == 0:
            return {
                'valve_report':[],
                'events':{
                    'valve1_events':[],
                    'valve2_events':[],
                },
                'summarization':[],
            }
        else:
            return {
                'valve_report':data,
                'events':{
                    'valve1_events':valve1_events,
                    'valve2_events':valve2_events,
                },
                'summarization':summarization,
            }

    def generate_location_history(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        device_reader = DeviceReader(unit)
        data = serializer.data
        for i in range(len(data)):
            data[i]['unit_name'] = unit.name
            data[i]['unit_description'] = unit.description
            data[i]['datetime'] = time_conversor.convert_utc_timestamp_to_local_datetimestr(
                data[i]['timestamp'],"%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(data[i]['attributes'])
            except:
                attributes = {}
            data[i]['attributes'] = attributes
            data[i]['ignition'] = device_reader.detect_ignition_event({
                'attributes':attributes
            })
            data[i]['odometer'] = device_reader.get_odometer({
                'attributes':attributes
            })
            data[i]['is_stop'] = False
        movement_events = self.calculate_unit_movement_events(unit,locations)
        stop_report = []
        for i in range(len(movement_events)):
            if i == 0:
                if movement_events[i]['event'] == 'START':
                    stop_duration = movement_events[i]['timestamp'] - initial_timestamp
                    stop_report.append({
                        'id': movement_events[i]['id'],
                        'latitude': movement_events[i]['latitude'],
                        'longitude': movement_events[i]['longitude'],
                        'stop_duration': stop_duration,
                        'stop_time': str(timedelta(seconds=stop_duration)),
                        'initial_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'final_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),

                    })
                elif  i == len(movement_events)-1 and movement_events[i]['event'] == 'STOP':
                    stop_duration = final_timestamp - movement_events[i]['timestamp']
                    stop_report.append({
                        'id': movement_events[i]['id'],
                        'latitude': movement_events[i]['latitude'],
                        'longitude': movement_events[i]['longitude'],
                        'stop_duration': stop_duration,
                        'stop_time': str(timedelta(seconds=stop_duration)),
                        'initial_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                    })
            else:
                if i == len(movement_events)-1 and movement_events[i]['event'] == 'STOP':
                    stop_duration = final_timestamp - movement_events[i]['timestamp']
                    stop_report.append({
                        'id': movement_events[i]['id'],
                        'latitude': movement_events[i]['latitude'],
                        'longitude': movement_events[i]['longitude'],
                        'stop_duration': stop_duration,
                        'stop_time': str(timedelta(seconds=stop_duration)),
                        'initial_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                    })
                elif movement_events[i-1]['event'] == 'STOP' and movement_events[i]['event'] == 'START':
                    stop_duration = movement_events[i]['timestamp'] - movement_events[i-1]['timestamp']
                    stop_report.append({
                        'id': movement_events[i-1]['id'],
                        'latitude': movement_events[i-1]['latitude'],
                        'longitude': movement_events[i-1]['longitude'],
                        'stop_duration': stop_duration,
                        'stop_time': str(timedelta(seconds=stop_duration)),
                        'initial_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i-1]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_stop_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                    })
        #print(stop_report)
        for item in data:
            for sr in stop_report:
                if item['id'] == sr['id']:
                    item['is_stop'] = True
                    item['stop_duration'] = sr['stop_duration']
                    item['stop_time'] = sr['stop_time']
                    item['initial_stop_datetime'] = sr['initial_stop_datetime']
                    item['final_stop_datetime'] = sr['final_stop_datetime']
                    break
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
        device_reader = DeviceReader(unit)
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
        if len(speed_report) > 0:
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                'number_of_speeds': len(speed_report)
            })
        return {
            'speed_report': speed_report,
            'summarization': summarization
        }

    def generate_long_speed_report(self,unit,initial_timestamp,final_timestamp,speed_limit):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        return self.calculate_long_speed_report(
            unit,
            initial_timestamp,
            final_timestamp,
            speed_limit,
            locations,
        )

    def generate_geofence_long_speed_report(self,unit,initial_timestamp,final_timestamp,geofences):
        speed_report = []
        summarization = []
        speed_list = []
        speed_list = list(dict.fromkeys([
            geofence.speed
            for geofence in geofences
            if geofence.enable_speed and geofence.speed != 0
        ]))
        if len(speed_list) == 0:
            return {
                'speed_report': speed_report,
                'summarization': summarization,
            }
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )

        def calculate_geofence_report(locations,geofence,initial_timestamp,final_timestamp):
                geofence_events = []
                geofence_report = []
                for i in range(len(locations)):
                    point = Point(locations[i]['longitude'],locations[i]['latitude'])
                    feature = json.loads(geofence.geojson)['features'][0]
                    s = shape(feature['geometry'])
                    if s.contains(point):
                        locations[i]['geofence_state'] = 1
                    else:
                        locations[i]['geofence_state'] = 0
                for i in range(len(locations)):
                    if i != 0:
                        previous_location = locations[i-1]
                        current_location = locations[i]
                        if previous_location['geofence_state'] == 0 and current_location['geofence_state'] == 1:
                            geofence_events.append({
                                'name': geofence.name,
                                'timestamp': locations[i]['timestamp'],
                                'speed': locations[i]['speed'],
                                'event': 'INPUT'
                            })
                        if previous_location['geofence_state'] == 1 and current_location['geofence_state'] == 0:
                            geofence_events.append({
                                'name': geofence.name,
                                'timestamp': locations[i]['timestamp'],
                                'speed': locations[i]['speed'],
                                'event': 'OUTPUT'
                            })
                
                for i in range(len(geofence_events)):
                    if i == 0:
                        if geofence_events[i]['event'] == 'OUTPUT':
                            duration = geofence_events[i]['timestamp'] - initial_timestamp
                            geofence_report.append({
                                'initial_timestamp': initial_timestamp,
                                'final_timestamp': geofence_events[i]['timestamp'],
                                'duration': duration,
                            })
                        elif i == len(geofence_events)-1 and geofence_events[i]['event'] == 'INPUT':
                            duration = final_timestamp - geofence_events[i]['timestamp']
                            geofence_report.append({
                                'initial_timestamp': geofence_events[i]['timestamp'],
                                'final_timestamp': final_timestamp,
                                'duration': duration,
                            })
                    else:
                        if i == len(geofence_events)-1 and geofence_events[i]['event'] == 'INPUT':
                            duration = final_timestamp - geofence_events[i]['timestamp']
                            geofence_report.append({
                                'initial_timestamp': geofence_events[i]['timestamp'],
                                'final_timestamp': final_timestamp,
                                'duration': duration,
                            })
                        else:
                            if geofence_events[i-1]['event'] == 'INPUT' and  geofence_events[i]['event'] == 'OUTPUT':
                                duration = geofence_events[i]['timestamp'] - geofence_events[i-1]['timestamp']
                                geofence_report.append({
                                    'initial_timestamp': geofence_events[i-1]['timestamp'],
                                    'final_timestamp': geofence_events[i]['timestamp'],
                                    'duration': duration,
                                })

                return geofence_report

        for speed in speed_list:
            long_speed_report = self.calculate_long_speed_report(
                unit,
                initial_timestamp,
                final_timestamp,
                speed,
                locations,
            )
            for lsr in long_speed_report['speed_report']:
                for geofence in geofences:
                    if geofence.speed == speed:
                        geofence_report = calculate_geofence_report(
                            lsr['positions'],
                            geofence,
                            lsr['initial_timestamp'],
                            lsr['final_timestamp'],
                        )
                        if len(geofence_report) > 0: print(geofence_report)
                        for gr in geofence_report:
                            new_positions = ([ position
                                for position in lsr['positions']
                                if
                                    position['timestamp'] >= gr['initial_timestamp'] and
                                    position['timestamp'] < gr['final_timestamp']
                            ])
                            new_speeds = [ position['speed'] for position in new_positions ]
                            distance = sum([
                                great_circle(
                                    (new_positions[i-1]['latitude'],new_positions[i-1]['longitude']),
                                    (new_positions[i]['latitude'],new_positions[i]['longitude']),
                                ).km
                                for i in range(len(new_positions))
                                    if i != 0
                            ])
                            speed_report.append({
                                'unit_name':unit.name,
                                'unit_description':unit.description,
                                'geofence_name':geofence.name,
                                'geofence_speed':geofence.speed,
                                'initial_latitude':new_positions[0]['latitude'],
                                'initial_longitude':new_positions[0]['longitude'],
                                'initial_timestamp':gr['initial_timestamp'],
                                'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                    gr['initial_timestamp'],"%d/%m/%Y %H:%M:%S"),
                                'initial_address':new_positions[0]['address'],
                                'final_latitude':new_positions[-1]['latitude'],
                                'final_longitude':new_positions[-1]['longitude'],
                                'final_timestamp':gr['final_timestamp'],
                                'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                    gr['final_timestamp'],"%d/%m/%Y %H:%M:%S"),
                                'final_address':new_positions[-1]['address'],
                                'speed_duration':gr['duration'],
                                'speed_time':str(timedelta(seconds=gr['duration'])),
                                'positions':new_positions,
                                'distance':round(distance,2),
                                'mean_speed':round(mean(new_speeds),2),
                                'max_speed':max(new_speeds),
                                'trespass_level':'LEVE',
                            })
        if len(speed_report) > 0:
            sumarization_geofences = list(dict.fromkeys([ sr['geofence_name'] for sr in speed_report ]))
            for summarization_geofence in sumarization_geofences:
                speed_counter = 0
                for sr in speed_report:
                    if sr['geofence_name'] == summarization_geofence:
                        speed_counter +=1
                summarization.append({
                    'unit_name': unit.name,
                    'unit_description': unit.description,
                    'geofence_name': summarization_geofence,
                    'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                        initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                    'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                        final_timestamp,"%d/%m/%Y %H:%M:%S"),
                    'number_of_speeds': speed_counter,
                })
        return {
            'speed_report': speed_report,
            'summarization': summarization,
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
                        'final_address':'N/D',
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
                        'final_address':'N/D',
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
                if len(movement_events) == 0: stop_duration = tr['trip_duration']
                tr['stop_duration'] = stop_duration
                tr['stop_time'] = str(timedelta(seconds=stop_duration))
                tr['driving_duration'] = tr['trip_duration'] - stop_duration
                tr['driving_time'] = str(timedelta(seconds=tr['driving_duration']))
        # CALCULAR GEOCERCAS
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
        # FIN - CALCULAR GEOCERCAS
        # CALCULAR RESUMEN
        if len(trip_report) > 0:
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
        return {
            'trip_report': trip_report,
            'summarization': summarization,
        }

    def generate_trip_report2(self,unit,initial_timestamp,final_timestamp,geofence_option):
        full_trip_report = []
        summarization = []
        initial_datetime_obj = datetime.utcfromtimestamp(initial_timestamp)
        initial_datetime_obj = gmt_conversor.convert_utctolocaltime(initial_datetime_obj)
        final_datetime_obj = datetime.utcfromtimestamp(final_timestamp)
        final_datetime_obj = gmt_conversor.convert_utctolocaltime(final_datetime_obj)
        datetime_ranges = []
        datetime_counter = initial_datetime_obj.replace(
            hour=0,minute=0,second=0)
        while datetime_counter < final_datetime_obj:
            datetime_ranges.append([
                datetime_counter,
                datetime_counter+timedelta(days=1)
            ])
            datetime_counter = datetime_counter+timedelta(days=1)
        datetime_ranges[0][0] = initial_datetime_obj
        datetime_ranges[len(datetime_ranges)-1][1] = final_datetime_obj
        for dr in datetime_ranges:
            trip_report = []
            timestamp1 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[0])))
            timestamp2 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[1])))
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=timestamp1,
                timestamp__lt=timestamp2
            ).order_by('timestamp').exclude(latitude=0.0,longitude=0.0)
            ignition_events = self.calculate_unit_ignition_events(unit,locations)
            for i in range(len(ignition_events)):
                if i == 0:
                    if ignition_events[i]['event'] == 'OFF':
                        trip_duration = ignition_events[i]['timestamp'] - timestamp1
                        trip_report.append({
                            'unit_name':unit.name,
                            'unit_description':unit.description,
                            'initial_latitude':'N/D',
                            'initial_longitude':'N/D',
                            'initial_timestamp':timestamp1,
                            'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                timestamp1,"%d/%m/%Y %H:%M:%S"),
                            'initial_address':'N/D',
                            'final_latitude':ignition_events[i]['latitude'],
                            'final_longitude':ignition_events[i]['longitude'],
                            'final_timestamp':ignition_events[i]['timestamp'],
                            'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                ignition_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                            'final_address':ignition_events[i]['address'],
                            'trip_duration':trip_duration,
                            'trip_time':str(timedelta(seconds=trip_duration)),
                        })
                    elif i == len(ignition_events)-1 and ignition_events[i]['event'] == 'ON':
                        trip_duration = timestamp2 - ignition_events[i]['timestamp']
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
                            'final_timestamp':timestamp2,
                            'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                timestamp2,"%d/%m/%Y %H:%M:%S"),
                            'trip_duration':trip_duration,
                            'trip_time':str(timedelta(seconds=trip_duration)),
                        })
                else:
                    if i == len(ignition_events)-1 and ignition_events[i]['event'] == 'ON':
                        trip_duration = timestamp2 - ignition_events[i]['timestamp']
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
                            'final_timestamp':timestamp2,
                            'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                timestamp2,"%d/%m/%Y %H:%M:%S"),
                            'trip_duration':trip_duration,
                            'trip_time':str(timedelta(seconds=trip_duration)),
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
                    """
                    trip_locations = ([ 
                        location 
                        for location in locations 
                        if location.timestamp < tr['final_timestamp']
                    ])
                    """
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
                    try:
                        average_speed = round(sum(speeds)/len(speeds),2)
                    except:
                        average_speed = 0
                    tr['average_speed'] = average_speed
                    try:
                        max_speed = max(speeds)
                    except:
                        max_speed = 0
                    tr['max_speed'] = max_speed
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
                    if len(movement_events) == 0: stop_duration = tr['trip_duration']
                    tr['stop_duration'] = stop_duration
                    tr['stop_time'] = str(timedelta(seconds=stop_duration))
                    tr['driving_duration'] = tr['trip_duration'] - stop_duration
                    tr['driving_time'] = str(timedelta(seconds=tr['driving_duration']))
            for tr in trip_report:
                full_trip_report.append(tr)
        # CALCULAR GEOCERCAS
        if geofence_option:
            geofences = Geofence.objects.filter(account=unit.account)
            for tr in full_trip_report:
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
            for tr in full_trip_report:
                tr['initial_geofences'] = 'N/D'
                tr['final_geofences'] = 'N/D'
        # FIN - CALCULAR GEOCERCAS
        # CALCULAR RESUMEN
        if len(full_trip_report) > 0:
            number_of_trips = 0
            distance_summarization = 0.0
            trip_duration_summarization = 0
            stop_duration_summarization = 0
            for tr in full_trip_report:
                if tr['initial_timestamp'] != 'N/D':
                    if tr['final_timestamp'] != 'N/D':
                        number_of_trips += 1
                        distance_summarization += tr['distance']
                        trip_duration_summarization += tr['trip_duration']
                        stop_duration_summarization += tr['stop_duration']
            driving_duration_summarization = trip_duration_summarization-stop_duration_summarization
            # CALCULANDO PORCENTAJES
            stop_percentage_summarization = stop_duration_summarization*100/trip_duration_summarization
            driving_percentage_summarization = 100 - stop_percentage_summarization
            # FIN - CALCULANDO PORCENTAJES
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
                #"trip_percentage_summarization": "",
                "stop_percentage_summarization": round(stop_percentage_summarization,2),
                "driving_percentage_summarization": round(driving_percentage_summarization,2),
            })
        # FIN - CALCULAR RESUMEN
        return {
            'trip_report': full_trip_report,
            'summarization': summarization,
        }

    def generate_mileage_report(self,unit,initial_timestamp,final_timestamp):
        day_mileage_report = []
        total_mileage_report = []
        initial_datetime_obj = datetime.utcfromtimestamp(initial_timestamp)
        initial_datetime_obj = gmt_conversor.convert_utctolocaltime(initial_datetime_obj)
        final_datetime_obj = datetime.utcfromtimestamp(final_timestamp)
        final_datetime_obj = gmt_conversor.convert_utctolocaltime(final_datetime_obj)
        datetime_ranges = []
        datetime_counter = initial_datetime_obj.replace(
            hour=0,minute=0,second=0)
        while datetime_counter < final_datetime_obj:
            datetime_ranges.append([
                datetime_counter,
                datetime_counter+timedelta(days=1)
            ])
            datetime_counter = datetime_counter+timedelta(days=1)
        datetime_ranges[0][0] = initial_datetime_obj
        datetime_ranges[len(datetime_ranges)-1][1] = final_datetime_obj
        total_distance_sum = 0.0
        for dr in datetime_ranges:
            timestamp1 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[0])))
            timestamp2 = int(datetime.timestamp(gmt_conversor.convert_localtimetoutc(dr[1])))
            locations = Location.objects.using('history_db_replica').filter(
                unitid=unit.id,
                timestamp__gte=timestamp1,
                timestamp__lt=timestamp2
            ).order_by('timestamp').exclude(latitude=0.0,longitude=0.0)
            distance_sum = 0.0
            for i in range(len(locations)):
                if i != 0:
                    distance = great_circle(
                        (
                            locations[i-1].latitude,
                            locations[i-1].longitude,
                        ),
                        (
                            locations[i].latitude,
                            locations[i].longitude,
                        ),
                    ).km
                    distance_sum += distance
            total_distance_sum += distance_sum
            day_mileage_report.append({
                'unit_name':unit.name,
                'unit_description':unit.description,
                'initial_datetime':dr[0].strftime("%d/%m/%Y %H:%M:%S"),
                'final_datetime':dr[1].strftime("%d/%m/%Y %H:%M:%S"),
                'distance':round(distance_sum,2)
            })
        if len(day_mileage_report) > 0:
            total_mileage_report.append({
                "unit_name":unit.name,
                "unit_description":unit.description,
                "initial_datetime":time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                "final_datetime":time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                "distance":round(total_distance_sum,2),
                "odometer":round(unit.odometer,2),
            })
        return {
            'total_mileage':total_mileage_report,
            'mileage_by_date':day_mileage_report,
        }

    def generate_geofence_report(self,unit,initial_timestamp,final_timestamp,geofences):
        geofence_report = []
        geofence_event_report = []
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        serializer = locations_serializers.LocationSerializer(locations,many=True)
        locations = serializer.data
        # CALCULAR SI SE ENCUENTRA EN GEOCERCA
        for i in range(len(locations)):
            point = Point(locations[i]['longitude'],locations[i]['latitude'])
            locations[i]['geofence_name'] = None
            locations[i]['geofence_id'] = None
            for geofence in geofences:
                feature = json.loads(geofence.geojson)['features'][0]
                s = shape(feature['geometry'])
                if s.contains(point):
                    locations[i]['geofence_name'] = geofence.name
                    locations[i]['geofence_id'] = geofence.id
                    break
        # FIN - CALCULAR SI SE ENCUENTRA EN GEOCERCA
        # CALCULAR EVENTO DE E/S DE GEOCERCA
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                if previous_location['geofence_name'] == None and current_location['geofence_name'] != None:
                    geofence_event_report.append({
                        'name': locations[i]['geofence_name'],
                        'timestamp': locations[i]['timestamp'],
                        'speed': locations[i]['speed'],
                        'event': 'INPUT'
                    })
                if previous_location['geofence_name'] != None and current_location['geofence_name'] == None:
                    geofence_event_report.append({
                        'name': locations[i-1]['geofence_name'],
                        'timestamp': locations[i]['timestamp'],
                        'speed': locations[i]['speed'],
                        'event': 'OUTPUT'
                    })
        # FIN - CALCULAR EVENTO DE E/S DE GEOCERCA
        for i in range(len(geofence_event_report)):
            if i == 0:
                if geofence_event_report[i]['event'] == 'OUTPUT':
                    duration = geofence_event_report[i]['timestamp'] - initial_timestamp
                    geofence_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'geofence_name': geofence_event_report[i]['name'],
                        'initial_timestamp': initial_timestamp,
                        'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'initial_speed': 'N/D',
                        'final_timestamp': geofence_event_report[i]['timestamp'],
                        'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            geofence_event_report[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_speed': geofence_event_report[i]['speed'],
                        'duration': duration,
                        'time': str(timedelta(seconds=duration)),
                    })
                elif i == len(geofence_event_report)-1 and geofence_event_report[i]['event'] == 'INPUT':
                    duration = final_timestamp - geofence_event_report[i]['timestamp']
                    geofence_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'geofence_name': geofence_event_report[i]['name'],
                        'initial_timestamp': geofence_event_report[i]['timestamp'],
                        'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            geofence_event_report[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_speed': geofence_event_report[i]['speed'],
                        'final_timestamp': final_timestamp,
                        'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'final_speed': 'N/D',
                        'duration': duration,
                        'time': str(timedelta(seconds=duration)),
                    })
            else:
                if i == len(geofence_event_report)-1 and geofence_event_report[i]['event'] == 'INPUT':
                    duration = final_timestamp - geofence_event_report[i]['timestamp']
                    geofence_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'geofence_name': geofence_event_report[i]['name'],
                        'initial_timestamp': geofence_event_report[i]['timestamp'],
                        'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            geofence_event_report[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'initial_speed': geofence_event_report[i]['speed'],
                        'final_timestamp': final_timestamp,
                        'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'final_speed': 'N/D',
                        'duration': duration,
                        'time': str(timedelta(seconds=duration)),
                    })
                else:
                    if geofence_event_report[i-1]['event'] == 'INPUT' and  geofence_event_report[i]['event'] == 'OUTPUT':
                        duration = geofence_event_report[i]['timestamp'] - geofence_event_report[i-1]['timestamp']
                        geofence_report.append({
                            'unit_name':unit.name,
                            'unit_description':unit.description,
                            'geofence_name': geofence_event_report[i]['name'],
                            'initial_timestamp': geofence_event_report[i-1]['timestamp'],
                            'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                geofence_event_report[i-1]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                            'initial_speed': geofence_event_report[i-1]['speed'],
                            'final_timestamp': geofence_event_report[i]['timestamp'],
                            'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                                geofence_event_report[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                            'final_speed': geofence_event_report[i]['speed'],
                            'duration': duration,
                            'time': str(timedelta(seconds=duration)),
                        })
        return geofence_report

    def generate_stop_report(self,unit,initial_timestamp,final_timestamp,geofence_option,discard_time):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lte=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        stop_report = []
        summarization = []
        movement_events = self.calculate_unit_movement_events(unit,locations)
        for i in range(len(movement_events)):
            if i == 0:
                if movement_events[i]['event'] == 'START':
                    stop_duration = movement_events[i]['timestamp'] - initial_timestamp
                    stop_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'latitude':movement_events[i]['latitude'],
                        'longitude':movement_events[i]['longitude'],
                        'initial_timestamp':initial_timestamp,
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'final_timestamp':movement_events[i]['timestamp'],
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'address':movement_events[i]['address'],
                        'stop_duration':stop_duration,
                        'stop_time':str(timedelta(seconds=stop_duration)),
                    })
                elif i == len(movement_events)-1 and movement_events[i]['event'] == 'STOP':
                    stop_duration =  final_timestamp - movement_events[i]['timestamp']
                    stop_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'latitude':movement_events[i]['latitude'],
                        'longitude':movement_events[i]['longitude'],
                        'initial_timestamp':movement_events[i]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_timestamp':final_timestamp,
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'address':movement_events[i]['address'],
                        'stop_duration':stop_duration,
                        'stop_time':str(timedelta(seconds=stop_duration)),
                    })
            else:
                if i == len(movement_events)-1 and movement_events[i]['event'] == 'STOP':
                    stop_duration =  final_timestamp - movement_events[i]['timestamp']
                    stop_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'latitude':movement_events[i]['latitude'],
                        'longitude':movement_events[i]['longitude'],
                        'initial_timestamp':movement_events[i]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_timestamp':final_timestamp,
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            final_timestamp,"%d/%m/%Y %H:%M:%S"),
                        'address':movement_events[i]['address'],
                        'stop_duration':stop_duration,
                        'stop_time':str(timedelta(seconds=stop_duration)),
                    })
                elif movement_events[i-1]['event'] == 'STOP' and movement_events[i]['event'] == 'START':
                    stop_duration = movement_events[i]['timestamp'] - movement_events[i-1]['timestamp']
                    stop_report.append({
                        'unit_name':unit.name,
                        'unit_description':unit.description,
                        'latitude':movement_events[i]['latitude'],
                        'longitude':movement_events[i]['longitude'],
                        'initial_timestamp':movement_events[i-1]['timestamp'],
                        'initial_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i-1]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'final_timestamp':movement_events[i]['timestamp'],
                        'final_datetime':time_conversor.convert_utc_timestamp_to_local_datetimestr(
                            movement_events[i]['timestamp'],"%d/%m/%Y %H:%M:%S"),
                        'address':movement_events[i]['address'],
                        'stop_duration':stop_duration,
                        'stop_time':str(timedelta(seconds=stop_duration))
                    })
        stop_report = list(filter(lambda x : x['stop_duration'] > discard_time, stop_report))
        # CALCULAR GEOCERCAS
        if geofence_option:
            geofences = Geofence.objects.filter(account=unit.account)
            for sr in stop_report:
                matching_geofences = []
                for geofence in geofences:
                    try:
                        geojson = json.loads(geofence.geojson)
                        if 'radius' in geojson['features'][0]['properties']:
                            lat = geojson['features'][0]['geometry']['coordinates'][1]
                            lon = geojson['features'][0]['geometry']['coordinates'][0]
                            radius = geojson['features'][0]['properties']['radius']
                            distance = great_circle(
                                (
                                    lat,
                                    lon,
                                ),
                                (
                                    sr['latitude'],
                                    sr['longitude'],
                                ),
                            ).meters
                            #print(distance)
                            if distance < radius:
                                matching_geofences.append(geofence.name)
                        else:
                            feature = geojson['features'][0]
                            s = shape(feature['geometry'])
                            point = Point(sr['longitude'],sr['latitude'])
                            if s.contains(point):
                                matching_geofences.append(geofence.name)
                    except Exception as e:
                        print(e)
                geofence_str = ""
                for i in range(len(matching_geofences)):
                    if i==0:
                        geofence_str += matching_geofences[i]
                    else:
                        geofence_str += f', {matching_geofences[i]}'
                sr['geofences'] = geofence_str
        else:
            for tr in stop_report:
                tr['geofences'] = 'N/D'
        # FIN - CALCULAR GEOCERCAS
        # CALCULAR RESUMEN
        if len(stop_report) > 0:
            stop_duration_list = list(map(lambda x : x['stop_duration'], stop_report))
            stop_duration_summarization = reduce(lambda x, y: x + y, stop_duration_list)
            summarization.append({
                "unit_name" : unit.name,
                "unit_description": unit.description,
                "initial_datetime": time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                "final_datetime" : time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                "number_of_stops": len(stop_report),
                "stop_duration_summarization": stop_duration_summarization,
            })
        # FIN - CALCULAR RESUMEN
        return {
                'stop_report': stop_report,
                'summarization': summarization,
            }

    def generate_temperature_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        temperature_report = []
        summarization = []
        temp_list = []
        device_reader = DeviceReader(unit)
        for location in locations:
            item = {
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    location.timestamp,"%d/%m/%Y %H:%M:%S"),
                'timestamp': location.timestamp,
                'latitude': location.latitude,
                'longitude': location.longitude,
                'speed': location.speed,
                'angle': location.angle,
                'ignition': device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                }),
                'address': location.address,
            }
            try:
                temp = float(json.loads(location.attributes)['temp1'])/0.1
                if int(temp) == 3000:
                    item['temp'] = int(temp)
                    temperature_report.append(item)
                    temp_list.append(int(temp))
                else:
                    item['temp'] = round(temp*0.001,2)
                    temperature_report.append(item)
                    temp_list.append(round(temp*0.001,2))
            except Exception as e:
                pass

        if len(temp_list) > 0:
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                'max_temp': max(temp_list),
                'min_temp': min(temp_list),
                'avg1_temp': round(mean(temp_list),2),
                'avg2_temp': round(median(temp_list),2)
            })
        return {
            'temperature_report':temperature_report,
            'summarization':summarization,
        }

    def generate_hours_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        hours_report = []
        summarization = []
        hours_list = []
        device_reader = DeviceReader(unit)
        for location in locations:
            item = {
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    location.timestamp,"%d/%m/%Y %H:%M:%S"),
                'latitude': location.latitude,
                'longitude': location.longitude,
                'speed': location.speed,
                'angle': location.angle,
                'ignition': device_reader.detect_ignition_event({
                    'attributes':json.loads(location.attributes)
                }),
                'address': location.address,
            }
            try:
                c_time = int(device_reader.get_hours({'attributes':json.loads(location.attributes)}))
                #c_time = int(json.loads(location.attributes)['io449'])
                if c_time > 0:
                    hours = int(c_time/3600)
                    minutes = int(c_time%3600/60)
                    item['hours'] = f"{hours} h {minutes} m"
                    hours_report.append(item)
                    hours_list.append(c_time)
            except Exception as e:
                print(e)
                pass
        if len(hours_list) > 0:
            c_time = max(hours_list) - min(hours_list)
            hours = int(c_time/3600)
            minutes = int(c_time%3600/60)
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                'hours': f"{hours} h {minutes} m",
            })
        return {
            'hours_report':hours_report,
            'summarization':summarization,
        }

    def generate_telemetry_report(self,unit,initial_timestamp,final_timestamp):
        locations = Location.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lt=final_timestamp
        ).order_by('timestamp').exclude(
            latitude=0.0,
            longitude=0.0
        )
        telemetry_report = []
        summarization = []
        rpm_list = []
        engine_coolant_temp_list = []
        ambient_air_temp_list = []
        acceleration_pedal_position_list = []
        engine_current_load_list = []
        engine_total_fuel_used_list = []
        fuel_level_list = []
        odometer_list = []
        speed_list = []
        accumulated_distance = 0.0
        device_reader = DeviceReader(unit)
        for i in range(len(locations)):
            if i > 0:
                distance = great_circle(
                    (
                        locations[i-1].latitude,
                        locations[i-1].longitude
                    ),
                    (
                        locations[i].latitude,
                        locations[i].longitude
                    ),
                ).km
                accumulated_distance += distance
            attributes = json.loads(locations[i].attributes)
            item = {
                'unit_name': unit.name,
                'unit_description': unit.description,
                'datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    locations[i].timestamp,"%d/%m/%Y %H:%M:%S"),
                'timestamp': locations[i].timestamp,
                'latitude': locations[i].latitude,
                'longitude': locations[i].longitude,
                'speed': locations[i].speed,
                'angle': locations[i].angle,
                'ignition': device_reader.detect_ignition_event({
                    'attributes':json.loads(locations[i].attributes)
                }),
                'accumulated_distance': accumulated_distance,
                'address': locations[i].address,
            }
            try:
                if locations[i].protocol == 'teltonika640':
                    item['rpm_engine'] = attributes['io88']
                    rpm_list.append(attributes['io88'])
                else:
                    item['rpm_engine'] = 'N/D'
            except Exception as e:
                item['rpm_engine'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['engine_coolant_temp'] = attributes['io127']
                    engine_coolant_temp_list.append(attributes['io127'])
                else:
                    item['engine_coolant_temp'] = 'N/D'
            except Exception as e:
                item['engine_coolant_temp'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['ambient_air_temp'] = attributes['io128']
                    ambient_air_temp_list.append(attributes['io128'])
                else:
                    item['ambient_air_temp'] = 'N/D'
            except Exception as e:
                item['ambient_air_temp'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    kms = attributes['io192']/1000
                    item['odometer'] = round(kms,2)
                    odometer_list.append(round(kms,2))
                else:
                    item['odometer'] = 'N/D'
            except Exception as e:
                item['odometer'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['acceleration_pedal_position'] = attributes['io84']
                    acceleration_pedal_position_list.append(attributes['io84'])
                else:
                    item['acceleration_pedal_position'] = 'N/D'
            except Exception as e:
                item['acceleration_pedal_position'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['engine_current_load'] = attributes['io85']
                    engine_current_load_list.append(attributes['io85'])
                else:
                    item['engine_current_load'] = 'N/D'
            except Exception as e:
                item['engine_current_load'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['engine_total_fuel_used'] = attributes['io86']
                    engine_total_fuel_used_list.append(attributes['io86'])
                else:
                    item['engine_total_fuel_used'] = 'N/D'
            except Exception as e:
                item['engine_total_fuel_used'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    item['fuel_level'] = attributes['io87']
                    fuel_level_list.append(attributes['io87'])
                else:
                    item['fuel_level'] = 'N/D'
            except Exception as e:
                item['fuel_level'] = 'N/D'
            try:
                if locations[i].protocol == 'teltonika640':
                    speed_list.append(item['speed'])
            except Exception as e:
                pass
            telemetry_report.append(item)

        if len(telemetry_report) > 0:
            try:
                max_rpm = max(rpm_list)
            except:
                max_rpm = "N/A"
            try:
                rpm_avg = round(mean([x for x in rpm_list if x != 0]),2)
            except:
                rpm_avg = "N/A"
            try:
                max_engine_coolant_temp = max(engine_coolant_temp_list)
            except:
                max_engine_coolant_temp = "N/A"
            try:
                max_ambient_air_temp = max(ambient_air_temp_list)
            except:
                max_ambient_air_temp = "N/A"
            try:
                max_acceleration_pedal_position = max(acceleration_pedal_position_list)
            except:
                max_acceleration_pedal_position = "N/A"
            try:
                max_engine_current_load = max(engine_current_load_list)
            except:
                max_engine_current_load = "N/A"
            try:
                fuel_used = max(engine_total_fuel_used_list) - min(engine_total_fuel_used_list)
            except:
                fuel_used = "N/A"
            try:
                max_fuel_level = max(fuel_level_list)
            except:
                max_fuel_level = "N/A"
            try:
                min_fuel_level = min(fuel_level_list)
            except:
                min_fuel_level = "N/A"
            try:
                mileage = round(max(odometer_list)-min(odometer_list),2)
            except:
                mileage = "N/A"
            try:
                initial_mileage = round(odometer_list[0],2)
            except:
                initial_mileage = "N/A"
            try:
                final_mileage = round(odometer_list[-1],2)
            except:
                final_mileage = "N/A"
            try:
                max_speed = round(max(speed_list),2)
            except:
                max_speed = "N/A"
            try:
                speed_avg = round(mean(speed_list),2)
            except:
                speed_avg = "N/A"
            try:
                fuel_economy = round(fuel_used/mileage,2)
            except:
                fuel_economy = "N/A"
            summarization.append({
                'unit_name': unit.name,
                'unit_description': unit.description,
                'initial_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    initial_timestamp,"%d/%m/%Y %H:%M:%S"),
                'final_datetime': time_conversor.convert_utc_timestamp_to_local_datetimestr(
                    final_timestamp,"%d/%m/%Y %H:%M:%S"),
                'max_rpm': max_rpm,
                'rpm_avg': rpm_avg,
                'max_engine_coolant_temp': max_engine_coolant_temp,
                'max_ambient_air_temp': max_ambient_air_temp,
                'max_acceleration_pedal_position': max_acceleration_pedal_position,
                'max_engine_current_load': max_engine_current_load,
                'fuel_used': fuel_used,
                'max_fuel_level': max_fuel_level,
                'min_fuel_level': min_fuel_level,
                'mileage': mileage,
                'initial_mileage': initial_mileage,
                'final_mileage': final_mileage,
                'max_speed': max_speed,
                'speed_avg': speed_avg,
                'fuel_economy': fuel_economy,
            })
        return {
            'telemetry_report':telemetry_report,
            'summarization':summarization,
        }