from units.models import Device
from alerts.models import Alert

from common.protocols.teltonika import Teltonika
from geofences.models import Geofence
from shapely.geometry import Point,shape
import json
import channels.layers
from asgiref.sync import async_to_sync

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

	def run(self,location):
		try:
			unit = Device.objects.get(uniqueid=self.deviceid)
			previous_location = json.loads(unit.previous_location)
			# ALERTA DE EVENTOS DE GEOCERCA
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
					'chat_PRUEBAS',
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
					'chat_PRUEBAS',
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

			# FIN ALERTA DE EVENTOS DE GEOCERCA
			
			# ALERTA DE VELOCIDAD

			# FIN ALERTA DE VELOCIDAD
		except Exception as e:
			file = open("/tmp/alert_log.log",'a')
			file.write(f"{str(e)}")
			file.close()
		