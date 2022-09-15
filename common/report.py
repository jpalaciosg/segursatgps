from datetime import datetime
from geopy.distance import great_circle
import json

from users.models import Device
from locations.models import Location
from locations import serializers as locations_serializers
from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader

gmt_conversor = GMTConversor()

class Report:

    def convert_datetimestr_to_timestamp(self,datetimestr):
        datetime_obj = datetime.strptime(datetimestr,'%Y-%m-%d %H:%M:%S')
        datetime_obj = gmt_conversor.convert_localtimetoutc(datetime_obj)
        timestamp = datetime.timestamp(datetime_obj)
        return timestamp

    def convert_timestamp_to_datetimestr(self,timestamp):
        datetime_obj = datetime.fromtimestamp(timestamp)
        datetime_obj = gmt_conversor.convert_utctolocaltime(datetime_obj)
        datetimestr = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        return datetimestr

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
            last_report = gmt_conversor.convert_utctolocaltime(datetime.utcfromtimestamp(data[i]['timestamp']))
            data[i]['datetime'] = last_report.strftime("%d/%m/%Y %H:%M:%S")
            try:
                attributes = json.loads(locations[i].attributes)
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
            dt = datetime.utcfromtimestamp(data[i]['timestamp'])
            dt = gmt_conversor.convert_utctolocaltime(dt)
            data[i]['datetime'] = dt.strftime("%d/%m/%Y %H:%M:%S")
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
            'initial_datetime': self.convert_timestamp_to_datetimestr(initial_timestamp),
            'final_datetime': self.convert_timestamp_to_datetimestr(final_timestamp),
            'type': 'harshAcceleration',
            'amount': harsh_acceleration
            },
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': self.convert_timestamp_to_datetimestr(initial_timestamp),
            'final_datetime': self.convert_timestamp_to_datetimestr(final_timestamp),
            'type': 'harshBraking',
            'amount': harsh_braking
            },
            {
            'unit_name': unit.name,
            'unit_description': unit.description,
            'initial_datetime': self.convert_timestamp_to_datetimestr(initial_timestamp),
            'final_datetime': self.convert_timestamp_to_datetimestr(final_timestamp),
            'type': 'harshCornering',
            'amount': harsh_cornering
            },
        ]
        final_report = {
            'harsh_driving_report':harsh_driving_report,
            'summarization':summarization,
        }
        return final_report


