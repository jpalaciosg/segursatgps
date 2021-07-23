from triggers.models import FleetTrigger
from units.models import Device
from alerts.models import Alert
from geofences.models import Geofence
from shapely.geometry import Point,shape

import json
from datetime import datetime
import channels.layers
from asgiref.sync import async_to_sync

from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor

gmt_conversor = GMTConversor() #conversor zona horaria

class AlertReader:
    def __init__(self, deviceid):
        self.deviceid = deviceid

    def __detect_geofence_event(self,current_location,previous_location):
        response = []
        geofences = Geofence.objects.all()
        for geofence in geofences:
            geojson = json.loads(geofence.geojson)
            s = shape(geojson['features'][0]['geometry'])
            point1 = Point(current_location['longitude'],current_location['latitude'])
            point2 = Point(previous_location['longitude'],previous_location['latitude'])
            if s.contains(point2) == False and s.contains(point1) == True:
                response.append({
                    "timestamp":current_location['timestamp'],
                    "latitude":current_location['latitude'],
                    "longitude":current_location['longitude'],
                    "speed":current_location['speed'],
                    "angle":current_location['angle'],
                    "alert_type":f"ALERTA DE INGRESO A GEOCERCA - {geofence.name}"
                })
            if s.contains(point2) == True and s.contains(point1) == False:
                response.append({
                    "timestamp":current_location['timestamp'],
                    "latitude":current_location['latitude'],
                    "longitude":current_location['longitude'],
                    "speed":current_location['speed'],
                    "angle":current_location['angle'],
                    "alert_type":f"ALERTA DE SALIDA DE GEOCERCA - {geofence.name}"
                })
        return response
    
    def __detect_battery_disconnection_alert(self,current_location,previous_location):
        device_reader = DeviceReader(self.deviceid)
        return device_reader.detect_battery_disconnection_event(current_location,previous_location)

    def __detect_speed_event(self,current_speed,speed_limit):
        if current_speed > speed_limit:
            return True
        else:
            return False

    def __detect_stop_event(self,last_movement,current_timestamp,seconds_limit):
        if last_movement == 0 or current_timestamp == 0:
            return False
        offset = current_timestamp - last_movement
        if offset > seconds_limit:
            return True
        else:
            return False

    def run(self):
        unit = Device.objects.get(uniqueid=self.deviceid)
        previous_location = json.loads(unit.previous_location)
        current_location = {
            'timestamp': unit.last_timestamp,
            'latitude': unit.last_latitude,
            'longitude': unit.last_longitude,
            'altitude': unit.last_altitude,
            'speed': unit.last_speed,
            'angle': unit.last_angle,
            'attributes': json.loads(unit.last_attributes)
        }
        triggers = FleetTrigger.objects.filter(account=unit.account)
        for trigger in triggers:
            # ALERTA DE VELOCIDAD GENERAL
            if trigger.alert_type == 1003:
                try:
                    #condition = json.loads(trigger.condition)
                    speed_limit = trigger.extension1003.speed
                    if self.__detect_speed_event(unit.last_speed,speed_limit):
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1003,
                            alert_description = "ALERTA DE EXCESO DE VELOCIDAD",
                            alert_priority = "H",
                            reference = unit.name,
                            accountid = unit.account.id
                        )
                        dt = datetime.fromtimestamp(alert.timestamp)
                        dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                        dt = dt.strftime("%d/%m/%Y %H:%M:%S")
                        channel_layer = channels.layers.get_channel_layer()
                        async_to_sync(channel_layer.group_send)(
                            f'chat_{unit.account.name}',
                            {
                                'type': 'send_message',
                                'message': {
                                    'type':'update_alert',
                                    'payload': {
                                        'unit_id': unit.id,
                                        'unit_name': unit.name,
                                        'unit_description': unit.description,
                                        'timestamp': alert.timestamp,
                                        'datetime': dt,
                                        'latitude': alert.latitude,
                                        'longitude': alert.longitude,
                                        'speed': alert.speed,
                                        'angle': alert.angle,
                                        'address': alert.address,
                                        'alert_type': alert.alert_type,
                                        'alert_description': alert.alert_description,
                                        'alert_priority': alert.alert_priority,
                                        'alert_id': alert.id
                                    }
                                }
                            }
                        )
                        async_to_sync(channel_layer.group_send)(
                            f'chat_{unit.account.name}',
                            {
                                'type': 'send_message',
                                'message': {
                                    'type':'notification',
                                    'payload': {
                                        'title': f'{unit.name} - {unit.description}',
                                        'message': alert.alert_description,
                                    }
                                }
                            }
                        )
                except Exception as e:
                    file = open("/tmp/alert_log.log",'a')
                    file.write(f"{str(e)}")
                    file.close()
            # FIN ALERTA DE VELOCIDAD GENERAL
            
            # ALERTA DE VELOCIDAD POR GEOCERCAS
            if trigger.alert_type == 1006:
                try:
                    speed_limit = trigger.extension1006.speed
                    if self.__detect_speed_event(unit.last_speed,speed_limit):
                        geofences = trigger.extension1006.geofences.all()
                        for geofence in geofences:
                            feature = json.loads(geofence.geojson)['features'][0]
                            s = shape(feature['geometry'])
                            point = Point(unit.last_longitude,unit.last_latitude)
                            if s.contains(point):
                                alert = Alert.objects.create(
                                    unitid = unit.id,
                                    timestamp = unit.last_timestamp,
                                    latitude = unit.last_latitude,
                                    longitude = unit.last_longitude,
                                    speed = unit.last_speed,
                                    angle = unit.last_angle,
                                    address = unit.last_address,
                                    alert_type = 1006,
                                    alert_description = f"ALERTA DE EXCESO DE VELOCIDAD - {geofence.name}",
                                    alert_priority = "H",
                                    reference = unit.name,
                                    accountid = unit.account.id
                                )
                                dt = datetime.fromtimestamp(alert.timestamp)
                                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                                dt = dt.strftime("%d/%m/%Y %H:%M:%S")
                                channel_layer = channels.layers.get_channel_layer()
                                async_to_sync(channel_layer.group_send)(
                                    f'chat_{unit.account.name}',
                                    {
                                        'type': 'send_message',
                                        'message': {
                                            'type':'update_alert',
                                            'payload': {
                                                'unit_id': unit.id,
                                                'unit_name': unit.name,
                                                'unit_description': unit.description,
                                                'timestamp': alert.timestamp,
                                                'datetime': dt,
                                                'latitude': alert.latitude,
                                                'longitude': alert.longitude,
                                                'speed': alert.speed,
                                                'angle': alert.angle,
                                                'address': alert.address,
                                                'alert_type': alert.alert_type,
                                                'alert_description': alert.alert_description,
                                                'alert_priority': alert.alert_priority,
                                                'alert_id': alert.id
                                            }
                                        }
                                    }
                                )
                                async_to_sync(channel_layer.group_send)(
                                    f'chat_{unit.account.name}',
                                    {
                                        'type': 'send_message',
                                        'message': {
                                            'type':'notification',
                                            'payload': {
                                                'title': f'{unit.name} - {unit.description}',
                                                'message': alert.alert_description,
                                            }
                                        }
                                    }
                                )
                except Exception as e:
                    file = open("/tmp/alert_log.log",'a')
                    file.write(f"{str(e)}")
                    file.close()
            # FIN ALERTA DE VELOCIDAD POR GEOCERCAS

            # ALERTA DE PARADA POR GEOCERCAS
            if trigger.alert_type == 1007:
                try:
                    seconds = trigger.extension1007.seconds
                    if self.__detect_stop_event(unit.last_movement,unit.last_timestamp,seconds):
                        geofences = trigger.extension1007.geofences.all()
                        for geofence in geofences:
                            feature = json.loads(geofence.geojson)['features'][0]
                            s = shape(feature['geometry'])
                            point = Point(unit.last_longitude,unit.last_latitude)
                            if s.contains(point):
                                alert = Alert.objects.create(
                                    unitid = unit.id,
                                    timestamp = unit.last_timestamp,
                                    latitude = unit.last_latitude,
                                    longitude = unit.last_longitude,
                                    speed = unit.last_speed,
                                    angle = unit.last_angle,
                                    address = unit.last_address,
                                    alert_type = 1007,
                                    alert_description = f"ALERTA DE PARADA EN GEOCERCA - {geofence.name}",
                                    alert_priority = "H",
                                    reference = unit.name,
                                    accountid = unit.account.id
                                )
                                dt = datetime.fromtimestamp(alert.timestamp)
                                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                                dt = dt.strftime("%d/%m/%Y %H:%M:%S")
                                channel_layer = channels.layers.get_channel_layer()
                                async_to_sync(channel_layer.group_send)(
                                    f'chat_{unit.account.name}',
                                    {
                                        'type': 'send_message',
                                        'message': {
                                            'type':'update_alert',
                                            'payload': {
                                                'unit_id': unit.id,
                                                'unit_name': unit.name,
                                                'unit_description': unit.description,
                                                'timestamp': alert.timestamp,
                                                'datetime': dt,
                                                'latitude': alert.latitude,
                                                'longitude': alert.longitude,
                                                'speed': alert.speed,
                                                'angle': alert.angle,
                                                'address': alert.address,
                                                'alert_type': alert.alert_type,
                                                'alert_description': alert.alert_description,
                                                'alert_priority': alert.alert_priority,
                                                'alert_id': alert.id
                                            }
                                        }
                                    }
                                )
                                async_to_sync(channel_layer.group_send)(
                                    f'chat_{unit.account.name}',
                                    {
                                        'type': 'send_message',
                                        'message': {
                                            'type':'notification',
                                            'payload': {
                                                'title': f'{unit.name} - {unit.description}',
                                                'message': alert.alert_description,
                                            }
                                        }
                                    }
                                )
                except Exception as e:
                    file = open("/tmp/alert_log.log",'a')
                    file.write(f"{str(e)}")
                    file.close()
            # FIN ALERTA DE PARADA POR GEOCERCAS