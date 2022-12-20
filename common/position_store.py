from django.db import connections

from datetime import datetime
import json

class PositionStore:
    #global datetime,connections
    def write(self,data):
        try:
            protocol = data['protocol']
            unitid = data['unit_id']
            accountid = data['account_id']
            timestamp = data['timestamp']
            latitude = data['latitude']
            longitude = data['longitude']
            altitude = data['altitude']
            angle = data['angle']
            speed = data['speed']
            attributes = data['attributes']
            address = data['address']
            reference_unit_name = data['unit_name']
            reference_account_name = data['account_name']
            date_str = datetime.utcfromtimestamp(timestamp).strftime("%Y%m%d")
            table_name = f"d{date_str}"
            query = (
                f"INSERT INTO {table_name}"
                "(protocol,unitid,accountid,timestamp,latitude,longitude,altitude,speed,angle,attributes,address,reference_unit_name,reference_account_name)"
                "VALUES"
                f"('{protocol}',{unitid},{accountid},{timestamp},{latitude},{longitude},{altitude},{speed},{angle},'{attributes}','{address}','{reference_unit_name}','{reference_account_name}')"
            )
            #print(query)
            cursor = connections['positiondb'].cursor()
            cursor.execute(query)
        except:
            pass
"""
position_store = PositionStore()
position_store.write({
    'protocol': 'generic',
    'unit_id': 1,
    'account_id': 1,
    'timestamp': 1671504459,
    'latitude': 0.0,
    'longitude': 0.0,
    'altitude': 0,
    'angle': 0,
    'speed': 0,
    'attributes': '{}',
    'address': '',
    'unit_name': 'PRUEBA',
    'account_name': 'pruebas',
})
"""