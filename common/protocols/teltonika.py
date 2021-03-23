from alerts.models import Trigger,Alert
from units.models import Device,DeviceDigitalInput

from datetime import datetime,timezone,timedelta
import requests
import json

GEOCODING_SERVER = '172.16.2.4'

class Teltonika:

    def __init__(self, deviceid):
        self.deviceid = deviceid

    def __check_ignition(self,attributes,input):
        try:
            if input == None:
                if 'ignition' in attributes:
                    if attributes['ignition']:
                        return True
                    else:
                        return False
                else:
                    print("Ignition does not exist.")
                    return False
            else:
                if input in attributes:
                    print(attributes[input])
                    if attributes[input] == 1:
                        return True
                    else:
                        return False
                else:
                    raise Exception(f"{input} does not exist.")
        except Exception as e:
            print(e)
            return False

    def detect_ignition_event(self,location):
        try:
            try:
                device_digital_input = DeviceDigitalInput.objects.get(
                    device__uniqueid=self.deviceid,
                    input_event="IGNITION"
                )
                input = device_digital_input.input
                input = f'di{input}'
            except:
                input = None
            attributes = location['attributes']
            return self.__check_ignition(attributes,input)
        except Exception as e:
            print(e)
            return False

    def detect_panic_event(self,location):
        try:
            device_digital_input = DeviceDigitalInput.objects.get(
                device__uniqueid=self.deviceid,
                input_event="PANIC"
            )
            input = device_digital_input.input
            input = f'di{input}'
            attributes = location['attributes']
            if input in attributes:
                if attributes[input] == 1:
                    return True
                elif attributes[input] == 0:
                    return False
            else:
                raise Exception(f"{input} does not exist.")
        except Exception as e:
            print(e)
            return False

    def get_stop_report(self,locations):
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
                        'initial_timestamp':locations[i]['timestamp'],
                    })
                elif previous_speed==0 and current_speed!=0:
                    #print('MOVEMENT')
                    if len(stop_report) == 0:
                        timestamp = locations[i]['timestamp']
                        dt_object = datetime.fromtimestamp(timestamp)
                        dt_str = dt_object.strftime("%d/%m/%Y, %H:%M:%S")
                        dt_str = dt_object.strftime("%d/%m/%Y, 00:00:00")
                        dt_object = datetime.strptime(dt_str, '%d/%m/%Y, %H:%M:%S')
                        initial_timestamp = int(dt_object.replace(tzinfo=timezone.utc).timestamp())
                        stop_report.append({
                            'latitude':locations[i]['latitude'],
                            'longitude':locations[i]['longitude'],
                            'initial_timestamp':initial_timestamp,
                            'final_timestamp':timestamp,
                        })
                    else:
                        stop_report[-1]['final_timestamp'] = locations[i]['timestamp']
        if len(stop_report) != 0:
            if "final_timestamp" not in stop_report[-1]:
                timestamp = stop_report[-1]['initial_timestamp']
                dt_object = datetime.fromtimestamp(timestamp)
                dt_str = dt_object.strftime("%d/%m/%Y, %H:%M:%S")
                dt_str = dt_object.strftime("%d/%m/%Y, 00:00:00")
                dt_object = datetime.strptime(dt_str, '%d/%m/%Y, %H:%M:%S')
                initial_timestamp = int(dt_object.replace(tzinfo=timezone.utc).timestamp())
                final_timestamp = initial_timestamp + 86400
                stop_report[-1]['final_timestamp'] = locations[i]['timestamp']

        for sr in stop_report:
            duration = sr['final_timestamp'] - sr['initial_timestamp']
            sr['duration'] = str(timedelta(seconds=duration))
            sr['initial_datetime'] = datetime.fromtimestamp(sr['initial_timestamp']).strftime("%d/%m/%Y, %H:%M:%S")
            sr['final_datetime'] = datetime.fromtimestamp(sr['final_timestamp']).strftime("%d/%m/%Y, %H:%M:%S")
            try:
                api_url = f"http://{GEOCODING_SERVER}/nominatim/reverse?format=jsonv2&lat={sr['latitude']}&lon={sr['longitude']}&addressdetails=1"
                headers = {'Content-Type': 'application/json'}
                response = requests.get(api_url, headers=headers)
                address = json.loads(response.content.decode('utf-8'))['display_name']
            except Exception as e:
                address = ""
            sr['address'] = address
            print(sr)

        return stop_report
"""
from common.protocols.teltonika import Teltonika
fm = Teltonika({
    'deviceid':'352093087864533',
    'attributes':{'event': 0, 'ignition': True, 'motion': False, 'workMode': 4, 'io200': 2, 'gpsStatus': 3, 'di1': 1},
})
fm.detect_ignition_event()
fm.detect_panic_event()
"""