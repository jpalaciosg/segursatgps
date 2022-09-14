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
        device_reader = DeviceReader(unit.uniqueid)
        data = serializer.data