from common.protocols.teltonika import Teltonika

class DeviceReader:
	def __init__(self, deviceid):
		self.deviceid = deviceid

	def detect_ignition_event(self,location):
		reader = Teltonika(self.deviceid)
		return reader.detect_ignition_event(location)

	def detect_panic_event(self,location):
		reader = Teltonika(self.deviceid)
		return reader.detect_panic_event(location)
	
	def generate_stop_report(self,locations):
		reader = Teltonika(self.deviceid)
		return reader.generate_stop_report(locations)

	def generate_travel_report(self,locations):
		reader = Teltonika(self.deviceid)
		return reader.generate_travel_report(locations)

	def generate_speed_report(self,locations,speed_limit):
		reader = Teltonika(self.deviceid)
		return reader.generate_speed_report(locations,speed_limit)