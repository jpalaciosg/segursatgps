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
            if previous_power > 10 and current_power < 1:
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

    def generate_trip_report(self,locations):
        travel_report = []
        for i in range(len(locations)):
            if i != 0:
                previous_location = locations[i-1]
                current_location = locations[i]
                #previous_ignition = previous_location['attributes']['ignition']
                #current_ignition = current_location['attributes']['ignition']
                previous_ignition = self.detect_ignition_event(previous_location)
                current_ignition = self.detect_ignition_event(current_location)
                if previous_ignition == False and current_ignition == True:
                    #print('ON')
                    travel_report.append({
                        'latitude':locations[i]['latitude'],
                        'longitude':locations[i]['longitude'],
                        'initial_timestamp':locations[i]['timestamp'],
                    })
                elif previous_ignition == True and current_ignition == False:
                    #print('OFF')
                    if len(travel_report) == 0:
                        timestamp = locations[i]['timestamp']
                        dt_object = datetime.fromtimestamp(timestamp)
                        dt_str = dt_object.strftime("%d/%m/%Y, %H:%M:%S")
                        dt_object = datetime.strptime(dt_str, '%d/%m/%Y, %H:%M:%S')
                        #initial_timestamp = int(dt_object.replace(tzinfo=timezone.utc).timestamp())
                        initial_timestamp = int(dt_object.timestamp())
                        travel_report.append({
                            'latitude':locations[i]['latitude'],
                            'longitude':locations[i]['longitude'],
                            'initial_timestamp':initial_timestamp,
                            'final_timestamp':timestamp,
                        })
                    else:
                        travel_report[-1]['final_timestamp'] = locations[i]['timestamp']

        if len(travel_report) != 0:
            if "final_timestamp" not in travel_report[-1]:
                timestamp = travel_report[-1]['initial_timestamp']
                dt_object = datetime.fromtimestamp(timestamp)
                dt_str = dt_object.strftime("%d/%m/%Y, %H:%M:%S")
                dt_object = datetime.strptime(dt_str, '%d/%m/%Y, %H:%M:%S')
                initial_timestamp = int(dt_object.replace(tzinfo=timezone.utc).timestamp())
                travel_report[-1]['final_timestamp'] = locations[i]['timestamp']

        for tr in travel_report:
            duration = tr['final_timestamp'] - tr['initial_timestamp']
            tr['duration'] = duration
            tr['time'] = str(timedelta(seconds=duration))
            tr['initial_datetime'] = datetime.fromtimestamp(tr['initial_timestamp'])
            tr['initial_datetime'] = gmt_conversor.convert_utctolocaltime(tr['initial_datetime']).strftime("%d/%m/%Y, %H:%M:%S")
            tr['final_datetime'] = datetime.fromtimestamp(tr['final_timestamp'])
            tr['final_datetime'] = gmt_conversor.convert_utctolocaltime(tr['final_datetime']).strftime("%d/%m/%Y, %H:%M:%S")
            speeds = []
            distance = 0
            for location in locations:
                if location['timestamp'] >= tr['initial_timestamp'] and location['timestamp'] <= tr['final_timestamp']:
                    speeds.append(location['speed'])
                if location['timestamp'] == tr['initial_timestamp']:
                    tr['initial_latitude'] = location['latitude']
                    tr['initial_longitude'] = location['longitude']
                    tr['initial_address'] = location['address']
                if location['timestamp'] == tr['final_timestamp']:
                    tr['final_latitude'] = location['latitude']
                    tr['final_longitude'] = location['longitude']
                    tr['final_address'] = location['address']
            average_speed = int(sum(speeds)/len(speeds))
            max_speed = max(speeds)
            tr['average_speed'] = average_speed
            tr['max_speed'] = max_speed
            for i in range(len(locations)):
                if i != 0:
                    if locations[i]['timestamp'] >= tr['initial_timestamp'] and locations[i]['timestamp'] <= tr['final_timestamp']:
                        previous_location = {
                            'latitude' : locations[i-1]['latitude'],
                            'longitude' : locations[i-1]['longitude'],
                        }
                        if locations[i]['latitude'] != 0.0 and locations[i]['longitude'] != 0.0:
                            distance2 = great_circle(
                                (
                                    previous_location['latitude'],
                                    previous_location['longitude']
                                ),
                                (
                                    locations[i]['latitude'],
                                    locations[i]['longitude']
                                ),
                            ).km
                        distance += distance2
                tr['distance'] = round(distance,2)

            for i in range(len(travel_report)):
                if travel_report[i]['duration'] < 5:
                    del travel_report[i]
        
        return travel_report