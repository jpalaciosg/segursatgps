from datetime import datetime,timedelta

class GMTConversor:
	def convert_utctolocaltime(self,dt):
		dt = dt - timedelta(hours=5)
		return dt
	def convert_localtimetoutc(self,dt):
		dt = dt + timedelta(hours=5)
		return dt