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
	
	def get_stop_report(self,locations):
		reader = Teltonika(self.deviceid)
		return reader.get_stop_report(locations)