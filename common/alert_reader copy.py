from units.models import Device
from alerts.models import Alert

#from common.protocols.teltonika import Teltonika
from common.device_reader import DeviceReader
from geofences.models import Geofence
from shapely.geometry import Point,shape
import json
import channels.layers
from asgiref.sync import async_to_sync

class AlertReader:
	def __init__(self, unit):
		self.unit = unit

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

	def __detect_speed_alert(self,speed_limit):
		if self.unit.last_speed > speed_limit:
			return True
		else:
			return False

	def run(self):
		previous_location = json.loads(self.unit.previous_location)
		current_location = {
			'timestamp': self.unit.last_timestamp,
			'latitude': self.unit.last_latitude,
			'longitude': self.unit.last_longitude,
			'altitude': self.unit.last_altitude,
			'speed': self.unit.last_speed,
			'angle': self.unit.last_angle,
			'attributes': json.loads(self.unit.last_attributes)
		}
		# ALERTA DE EVENTOS DE GEOCERCA
		"""
		try:
			unit = Device.objects.get(uniqueid=self.deviceid)
			previous_location = json.loads(unit.previous_location)
			event_geofence_result = self.__detect_geofence_event(location,previous_location)
			for item in event_geofence_result:
				alert = Alert.objects.create(
					unitid = unit.id,
					timestamp = item['timestamp'],
					latitude = item['latitude'],
					longitude = item['longitude'],
					speed = item['speed'],
					angle = item['angle'],
					alert_type = item['alert_type'],
					alert_priority = "M",
					account = unit.account
				)
				channel_layer = channels.layers.get_channel_layer()
				async_to_sync(channel_layer.group_send)(
					f'chat_{unit.account.name}',
					{
						'type': 'send_message',
						'message': {
							'type':'update_alert',
							'payload': {
								'unitid': unit.id,
								'unit_name': unit.name,
								'timestamp': alert.timestamp,
								'latitude': alert.latitude,
								'longitude': alert.longitude,
								'speed': alert.speed,
								'angle': alert.angle,
								'alert_type': alert.alert_type,
								'alert_priority': alert.alert_priority 
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
								'title': unit.name,
								'message': alert.alert_type,
							}
						}
					}
				)
		except Exception as e:
			file = open("/tmp/alert_log.log",'a')
			file.write(f"{str(e)}")
			file.close()
		"""
		# FIN ALERTA DE EVENTOS DE GEOCERCA
		# ALERTA DE DESCONEXION DE BATERIA
		"""
		try:
			if self.__detect_battery_disconnection_alert(self,current_location,previous_location):
				alert = Alert.objects.create(
					unitid = self.unit.id,
					timestamp = self.unit.last_timestamp,
					latitude = self.unit.last_latitude,
					longitude = self.unit.last_longitude,
					speed = self.unit.last_speed,
					angle = self.unit.last_angle,
					alert_type = "ALERTA DE DESCONEXION DE BATERIA",
					alert_priority = "H",
					account = self.unit.account
				)
				channel_layer = channels.layers.get_channel_layer()
				async_to_sync(channel_layer.group_send)(
					f'chat_{self.unit.account.name}',
					{
						'type': 'send_message',
						'message': {
							'type':'update_alert',
							'payload': {
								'unitid': self.unit.id,
								'unit_name': self.unit.name,
								'timestamp': alert.timestamp,
								'latitude': alert.latitude,
								'longitude': alert.longitude,
								'speed': alert.speed,
								'angle': alert.angle,
								'alert_type': alert.alert_type,
								'alert_priority': alert.alert_priority 
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
								'title': unit.name,
								'message': alert.alert_type,
							}
						}
					}
				)
		except Exception as e:
			file = open("/tmp/alert_log.log",'a')
			file.write(f"{str(e)}")
			file.close()
		"""
		# FIN ALERTA DE DESCONEXION DE BATERIA
		# ALERTA DE VELOCIDAD GENERAL
		try:
			if self.__detect_speed_alert(90):
				alert = Alert.objects.create(
					unitid = self.unit.id,
					timestamp = self.unit.last_timestamp,
					latitude = self.unit.last_latitude,
					longitude = self.unit.last_longitude,
					speed = self.unit.last_speed,
					angle = self.unit.last_angle,
					alert_type = "ALERTA DE EXCESO DE VELOCIDAD",
					alert_priority = "H",
					#account = self.unit.account.name
				)
				channel_layer = channels.layers.get_channel_layer()
				async_to_sync(channel_layer.group_send)(
					f'chat_{self.unit.account.name}',
					{
						'type': 'send_message',
						'message': {
							'type':'update_alert',
							'payload': {
								'unit_id': self.unit.id,
								'unit_name': self.unit.name,
								'timestamp': alert.timestamp,
								'latitude': alert.latitude,
								'longitude': alert.longitude,
								'speed': alert.speed,
								'angle': alert.angle,
								'alert_type': alert.alert_type,
								'alert_priority': alert.alert_priority,
								'alert_id': alert.id
							}
						}
					}
				)
				async_to_sync(channel_layer.group_send)(
					f'chat_{self.unit.account.name}',
					{
						'type': 'send_message',
						'message': {
							'type':'notification',
							'payload': {
								'title': self.unit.name,
								'message': alert.alert_type,
							}
						}
					}
				)
		except Exception as e:
			file = open("/tmp/alert_log.log",'a')
			file.write(f"{str(e)}")
			file.close()
		# FIN ALERTA DE VELOCIDAD GENERAL