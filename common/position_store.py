from django.db import connections

from datetime import datetime,timedelta
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
            # limpiar strings
            address = address.replace("'","\'\'")
            # fin - limpiar strings
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
    
    def read(self,unitid,accountid,initial_timestamp,final_timestamp):
        initial_datetime_obj = datetime.utcfromtimestamp(initial_timestamp)
        final_datetime_obj = datetime.utcfromtimestamp(final_timestamp)
        datetime_ranges = []
        datetime_counter = initial_datetime_obj.replace(
            hour=0,minute=0,second=0)
        while datetime_counter < final_datetime_obj:
            datetime_ranges.append([
                datetime_counter,
                datetime_counter+timedelta(days=1)
            ])
            datetime_counter = datetime_counter+timedelta(days=1)
        if len(datetime_ranges) > 0:
            datetime_ranges[0][0] = initial_datetime_obj
            datetime_ranges[len(datetime_ranges)-1][1] = final_datetime_obj
        positions = []
        for dr in datetime_ranges:
            try:
                timestamp1 = int(datetime.timestamp(dr[0]))
                timestamp2 = int(datetime.timestamp(dr[1]))
                year = dr[0].year
                month = dr[0].month
                day = dr[0].day
                table_name = f"d{year}{month}{day}"
                query = (
                    f"SELECT * FROM {table_name} "
                    f"WHERE unitid={unitid} AND accountid={accountid} AND "
                    f"timestamp>={timestamp1} AND timestamp<{timestamp2}"
                )
                cursor = connections['positiondb'].cursor()
                cursor.execute(query)
                headers = [x[0] for x in cursor.description]
                result = cursor.fetchall()
                for item in result:
                    positions.append(dict(zip(headers,item)))
            except Exception as e:
                #print(e)
                pass
        positions = ([ 
            position for position in positions 
            if position['latitude'] !=0.0 and position['longitude'] !=0.0
        ])
        return positions