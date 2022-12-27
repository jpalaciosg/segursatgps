from django.db import connections

from datetime import datetime
import json

class PositionStore:
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
            attributes = json.dumps(data['attributes'])
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
        except Exception as e:
            """
            f = open('/tmp/positionstore.log','a')
            f.write(str(e))
            f.write('\n')
            f.close()
            """
            pass