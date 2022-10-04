from datetime import datetime

from common.gmt_conversor import GMTConversor
from common.device_reader import DeviceReader

gmt_conversor = GMTConversor()

class TimeConversor:

    def convert_seconds_in_hour_format(self,seconds):
        duration_hour = seconds/3600
        duration_minute = (duration_hour-int(duration_hour))*60
        duration_second = (duration_minute-int(duration_minute))*60
        duration_hour_str = str(int(duration_hour)) if int(duration_hour) >= 10 else '0'+str(int(duration_hour))
        duration_minute_str = str(int(duration_minute)) if int(duration_minute) >= 10 else '0'+str(int(duration_minute))
        duration_second_str = str(int(duration_second)) if int(duration_second) >= 10 else '0'+str(int(duration_second))
        duration_time_str = duration_hour_str+':'+duration_minute_str+':'+duration_second_str
        return duration_time_str

    def convert_local_datetimestr_to_utc_timestamp(self,datetimestr,format_code):
        #datetime_obj = datetime.strptime(datetimestr,'%Y-%m-%d %H:%M:%S')
        datetime_obj = datetime.strptime(datetimestr,format_code)
        datetime_obj = gmt_conversor.convert_localtimetoutc(datetime_obj)
        timestamp = datetime.timestamp(datetime_obj)
        return timestamp

    def convert_utc_timestamp_to_local_datetimestr(self,timestamp,format_code):
        datetime_obj = datetime.fromtimestamp(timestamp)
        datetime_obj = gmt_conversor.convert_utctolocaltime(datetime_obj)
        #datetimestr = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        datetimestr = datetime_obj.strftime(format_code)
        return datetimestr