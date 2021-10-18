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
