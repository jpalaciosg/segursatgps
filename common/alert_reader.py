from triggers.models import FleetTrigger
from units.models import Device,LastAlert
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

    def __detect_geofence_entry(self,current_location,previous_location):
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
        return response

    def __detect_geofence_exit(self,current_location,previous_location):
        response = []
        geofences = Geofence.objects.all()
        for geofence in geofences:
            geojson = json.loads(geofence.geojson)
            s = shape(geojson['features'][0]['geometry'])
            point1 = Point(current_location['longitude'],current_location['latitude'])
            point2 = Point(previous_location['longitude'],previous_location['latitude'])
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

    def __detect_panic_event(self,current_location):
        device_reader = DeviceReader(self.deviceid)
        return device_reader.detect_panic_event(current_location)

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

    def __detect_harsh_acceleration_event(self,current_location):
        device_reader = DeviceReader(self.deviceid)
        return device_reader.detect_harsh_acceleration_event(current_location)

    def __detect_harsh_braking_event(self,current_location):
        device_reader = DeviceReader(self.deviceid)
        return device_reader.detect_harsh_braking_event(current_location)

    def __detect_harsh_cornering_event(self,current_location):
        device_reader = DeviceReader(self.deviceid)
        return device_reader.detect_harsh_cornering_event(current_location)

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
            # ALERTA DE PANICO
            if trigger.alert_type == 1001:
                try:
                    if self.__detect_panic_event(current_location):
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1001
                            last_alert.alert_description = "ALERTA DE PANICO"
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1001,
                                alert_description = "ALERTA DE PANICO",
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1001,
                            alert_description = "ALERTA DE PANICO",
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    file = open("/tmp/panic_log.log",'a')
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN ALERTA DE PANICO
            # ALERTA DE DESCONEXION DE BATERIA
            if trigger.alert_type == 1002:
                try:
                    if self.__detect_battery_disconnection_alert(current_location,previous_location):
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1002
                            last_alert.alert_description = "ALERTA DE DESCONEXION DE BATERIA"
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1002,
                                alert_description = "ALERTA DE DESCONEXION DE BATERIA",
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            ) 
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1002,
                            alert_description = "ALERTA DE DESCONEXION DE BATERIA",
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN ALERTA DE DESCONEXION DE BATERIA
            
            # ALERTA DE VELOCIDAD GENERAL
            if trigger.alert_type == 1003:
                try:
                    #condition = json.loads(trigger.condition)
                    speed_limit = trigger.extension1003.speed
                    if self.__detect_speed_event(unit.last_speed,speed_limit):
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1003
                            last_alert.alert_description = "ALERTA DE EXCESO DE VELOCIDAD"
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1003,
                                alert_description = "ALERTA DE EXCESO DE VELOCIDAD",
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
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
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN ALERTA DE VELOCIDAD GENERAL
            
            # ALERTA DE INGRESO A GEOCERCA
            if trigger.alert_type == 1004:
                try:
                    events = self.__detect_geofence_entry(current_location,previous_location)
                    for event in events:
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1004
                            last_alert.alert_description = event['alert_type']
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1004,
                                alert_description = event['alert_type'],
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1004,
                            alert_description = event['alert_type'],
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    print(e)
            # FIN ALERTA DE INGRESO A GEOCERCA

            # ALERTA DE SALIDA GEOCERCA
            if trigger.alert_type == 1005:
                try:
                    events = self.__detect_geofence_exit(current_location,previous_location)
                    for event in events:
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1005
                            last_alert.alert_description = event['alert_type']
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1005,
                                alert_description = event['alert_type'],
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1005,
                            alert_description = event['alert_type'],
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    print(e)
            # FIN ALERTA DE SALIDA GEOCERCA

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
                                # ACTUALIZAR ULTIMA ALERTA
                                try:
                                    last_alert = LastAlert.objects.get(unit__id=unit.id)
                                except:
                                    last_alert = None
                                if last_alert:
                                    last_alert.timestamp = unit.last_timestamp
                                    last_alert.latitude = unit.last_latitude
                                    last_alert.longitude = unit.last_longitude
                                    last_alert.speed = unit.last_speed
                                    last_alert.angle = unit.last_angle
                                    last_alert.address = unit.last_address
                                    last_alert.alert_type = 1006
                                    last_alert.alert_description = f"ALERTA DE EXCESO DE VELOCIDAD - {geofence.name}"
                                    last_alert.alert_priority = trigger.alert_priority
                                    last_alert.account = unit.account
                                    last_alert.save()
                                else:
                                    last_alert = LastAlert.objects.create(
                                        unit = unit,
                                        timestamp = unit.last_timestamp,
                                        latitude = unit.last_latitude,
                                        longitude = unit.last_longitude,
                                        speed = unit.last_speed,
                                        angle = unit.last_angle,
                                        address = unit.last_address,
                                        alert_type = 1006,
                                        alert_description = f"ALERTA DE EXCESO DE VELOCIDAD - {geofence.name}",
                                        alert_priority = trigger.alert_priority,
                                        account = unit.account
                                    )  
                                # FIN - ACTUALIZAR ULTIMA ALERTA
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
                                    alert_priority = trigger.alert_priority,
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
                                if trigger.send_notification:
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
                    file.write(f"{str(e)}\n")
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
                                # ACTUALIZAR ULTIMA ALERTA
                                check = False
                                try:
                                    last_alert = LastAlert.objects.get(unit__id=unit.id)
                                except:
                                    last_alert = None
                                if last_alert:
                                    offset = unit.last_timestamp - last_alert.timestamp
                                    if offset > trigger.extension1007.seconds:
                                        last_alert.timestamp = unit.last_timestamp
                                        last_alert.latitude = unit.last_latitude
                                        last_alert.longitude = unit.last_longitude
                                        last_alert.speed = unit.last_speed
                                        last_alert.angle = unit.last_angle
                                        last_alert.address = unit.last_address
                                        last_alert.alert_type = 1007
                                        last_alert.alert_description = f"ALERTA DE PARADA EN GEOCERCA - {geofence.name}"
                                        last_alert.alert_priority = trigger.alert_priority
                                        last_alert.account = unit.account
                                        last_alert.save()
                                        check = True
                                else:
                                    last_alert = LastAlert.objects.create(
                                        unit = unit,
                                        timestamp = unit.last_timestamp,
                                        latitude = unit.last_latitude,
                                        longitude = unit.last_longitude,
                                        speed = unit.last_speed,
                                        angle = unit.last_angle,
                                        address = unit.last_address,
                                        alert_type = 1007,
                                        alert_description = f"ALERTA DE PARADA EN GEOCERCA - {geofence.name}",
                                        alert_priority = trigger.alert_priority,
                                        account = unit.account
                                    )
                                    check = True  
                                # FIN - ACTUALIZAR ULTIMA ALERTA
                                # INSERTAR ALERTA EN EL HISTORIAL
                                if check:
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
                                        alert_priority = trigger.alert_priority,
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
                                    if trigger.send_notification:
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
                                # FIN INSERTAR ALERTA EN EL HISTORIAL
                except Exception as e:
                    file = open("/tmp/alert_log.log",'a')
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN ALERTA DE PARADA POR GEOCERCAS

            # ALERTA DE ALERTA DE ACELERACION BRUSCA
            if trigger.alert_type == 1009:
                try:
                    if self.__detect_harsh_acceleration_event(current_location):
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1009
                            last_alert.alert_description = "ALERTA DE ACELERACION BRUSCA"
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1009,
                                alert_description = "ALERTA DE ACELERACION BRUSCA",
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1009,
                            alert_description = "ALERTA DE ACELERACION BRUSCA",
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN - ALERTA DE ALERTA DE ACELERACION BRUSCA

            # ALERTA DE ALERTA DE FRENADO BRUSCO
            if trigger.alert_type == 1010:
                try:
                    if self.__detect_harsh_braking_event(current_location):
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1010
                            last_alert.alert_description = "ALERTA DE FRENADO BRUSCO"
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1010,
                                alert_description = "ALERTA DE FRENADO BRUSCO",
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1010,
                            alert_description = "ALERTA DE FRENADO BRUSCO",
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN - ALERTA DE ALERTA DE FRENADO BRUSCO

            # ALERTA DE ALERTA DE GIRO BRUSCO
            if trigger.alert_type == 1011:
                try:
                    if self.__detect_harsh_cornering_event(current_location):
                        # ACTUALIZAR ULTIMA ALERTA
                        try:
                            last_alert = LastAlert.objects.get(unit__id=unit.id)
                        except:
                            last_alert = None
                        if last_alert:
                            last_alert.timestamp = unit.last_timestamp
                            last_alert.latitude = unit.last_latitude
                            last_alert.longitude = unit.last_longitude
                            last_alert.speed = unit.last_speed
                            last_alert.angle = unit.last_angle
                            last_alert.address = unit.last_address
                            last_alert.alert_type = 1011
                            last_alert.alert_description = "ALERTA DE GIRO BRUSCO"
                            last_alert.alert_priority = trigger.alert_priority
                            last_alert.account = unit.account
                            last_alert.save()
                        else:
                            last_alert = LastAlert.objects.create(
                                unit = unit,
                                timestamp = unit.last_timestamp,
                                latitude = unit.last_latitude,
                                longitude = unit.last_longitude,
                                speed = unit.last_speed,
                                angle = unit.last_angle,
                                address = unit.last_address,
                                alert_type = 1011,
                                alert_description = "ALERTA DE GIRO BRUSCO",
                                alert_priority = trigger.alert_priority,
                                account = unit.account
                            )  
                        # FIN - ACTUALIZAR ULTIMA ALERTA
                        alert = Alert.objects.create(
                            unitid = unit.id,
                            timestamp = unit.last_timestamp,
                            latitude = unit.last_latitude,
                            longitude = unit.last_longitude,
                            speed = unit.last_speed,
                            angle = unit.last_angle,
                            address = unit.last_address,
                            alert_type = 1011,
                            alert_description = "ALERTA DE GIRO BRUSCO",
                            alert_priority = trigger.alert_priority,
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
                        if trigger.send_notification:
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
                    file.write(f"{str(e)}\n")
                    file.close()
            # FIN - ALERTA DE ALERTA DE GIRO BRUSCO