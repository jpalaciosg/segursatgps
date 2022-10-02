from alerts.models import Alert
from units.models import Device,DeviceDigitalInput,DeviceDigitalOutput

from datetime import datetime,timezone,timedelta
import requests
import json
from geopy.distance import great_circle

from common.gmt_conversor import GMTConversor

GEOCODING_SERVER = '172.16.2.4'

gmt_conversor = GMTConversor()

class Teltonika:

    def __init__(self, deviceid):
        self.deviceid = deviceid

    def __check_ignition(self,attributes,ignition_source):
        if ignition_source in attributes:
            #print(attributes[ignition_source])
            if attributes[ignition_source] == 1:
                return True
            else:
                return False
        else:
            return False

    def __check_panic(self,attributes,panic_source):
        if panic_source in attributes:
            #print(attributes[panic_source])
            if attributes[panic_source] == 1:
                return True
            else:
                return False
        else:
            return False


    def detect_ignition_event(self,location):
        try:
            unit = Device.objects.get(
                uniqueid=self.deviceid
            )
            ignition_source = unit.ignition_source
            attributes = location['attributes']
            return self.__check_ignition(attributes,ignition_source)
        except Exception as e:
            print(e)
            return False

    def detect_panic_event(self,location):
        try:
            unit = Device.objects.get(
                uniqueid=self.deviceid
            )
            panic_source = unit.panic_source
            attributes = location['attributes']
            return self.__check_panic(attributes,panic_source)
        except Exception as e:
            print(e)
            return False

    def detect_battery_disconnection_event(self,current_location,previous_location):
        try:
            previous_power = float(previous_location['attributes']['power'])
            current_power = float(current_location['attributes']['power'])
            if previous_power > 1 and current_power < 1:
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def detect_motor_lock_event(self,location):
        try:
            try:
                device_digital_output = DeviceDigitalOutput.objects.get(
                    device__uniqueid=self.deviceid,
                    input_event="MOTOR_LOCK"
                )
                output = device_digital_output.output
                output = f'out{output}'
            except:
                input = None
            attributes = location['attributes']
            if input != None and input in attributes:
                print(attributes[input])
                if attributes[input] == True:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def detect_harsh_acceleration_event(self,location):
        try:
            attributes = location['attributes']
            if 'alarm' in attributes:
                if attributes['alarm'] == 'hardAcceleration':
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def detect_harsh_braking_event(self,location):
        try:
            attributes = location['attributes']
            if 'alarm' in attributes:
                if attributes['alarm'] == 'hardBraking':
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def detect_harsh_cornering_event(self,location):
        try:
            attributes = location['attributes']
            if 'alarm' in attributes:
                if attributes['alarm'] == 'hardCornering':
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def get_odometer(self,location):
        try:
            odometer = location['attributes']['odometer']
            odometer = float(odometer)/1000
            return odometer
        except:
            return 0

    def get_hours(self,location):
        try:
            hours = location['attributes']['io449']
            return hours
        except Exception as e:
            print(e)
            return 0

    def generate_stop_report(self,locations,initial_timestamp,final_timestamp,seconds):
        stop_report = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                previous_speed = previous_location['speed']
                current_speed = current_location['speed']
                if previous_speed!=0 and current_speed==0:
                    #print('STOP')
                    stop_report.append({
                        'latitude':locations[i]['latitude'],
                        'longitude':locations[i]['longitude'],
                        'angle':locations[i]['angle'],
                        'address':locations[i]['address'],
                        'initial_timestamp':locations[i]['timestamp'],
                    })
                elif previous_speed==0 and current_speed!=0:
                    #print('MOVEMENT')
                    if len(stop_report) == 0:
                        stop_report.append({
                            'latitude':locations[i]['latitude'],
                            'longitude':locations[i]['longitude'],
                            'angle':locations[i]['angle'],
                            'address':locations[i]['address'],
                            'initial_timestamp':initial_timestamp,
                            'final_timestamp':locations[i]['timestamp'],
                        })
                    else:
                        stop_report[-1]['final_timestamp'] = locations[i]['timestamp']
                    
        if len(stop_report) != 0:
            if "final_timestamp" not in stop_report[-1]:
                #stop_report[-1]['final_timestamp'] = locations[i]['timestamp']
                stop_report[-1]['final_timestamp'] = final_timestamp

        final_stop_report = []
        for sr in stop_report:
            duration = sr['final_timestamp'] - sr['initial_timestamp']
            if duration > seconds:
                sr['duration'] = duration
                sr['time'] = str(timedelta(seconds=duration))
                sr['initial_datetime'] = datetime.fromtimestamp(sr['initial_timestamp'])
                sr['initial_datetime'] = gmt_conversor.convert_utctolocaltime(sr['initial_datetime']).strftime("%d/%m/%Y %H:%M:%S")
                sr['final_datetime'] = datetime.fromtimestamp(sr['final_timestamp'])
                sr['final_datetime'] = gmt_conversor.convert_utctolocaltime(sr['final_datetime']).strftime("%d/%m/%Y %H:%M:%S")
                final_stop_report.append(sr)
        
        return final_stop_report