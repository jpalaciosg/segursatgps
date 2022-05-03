from async_timeout import current_task
from triggers.models import FleetTrigger
from units.models import Device
from datetime import datetime

fleet_triggers = FleetTrigger.objects.filter(alert_type=1012)

for trigger in fleet_triggers:
    try:
        units = Device.objects.filter(account=trigger.account)
        seconds = trigger.extension1012.seconds
        for unit in units:
            print(unit.name)
            print(unit.last_timestamp)
            print('-----------------')
            current_timestamp = int(datetime.now().timestamp())
            offset = current_timestamp - unit.last_timestamp
            if offset > seconds:
                print('bingo')
                """
                # ACTUALIZAR ULTIMA ALERTA
                try:
                    last_alert = LastAlert.objects.get(unit__id=unit.id)
                except:
                    last_alert = None
                if last_alert:
                    last_alert.timestamp = unit.last_timestamp
                    last_alert.latitude = unit.last_latitude
                    last_alert.longitude = unit.last_longitude
                    last_alert.speed = unit.last_speed
                    last_alert.angle = unit.last_angle
                    last_alert.address = unit.last_address
                    last_alert.alert_type = 1011
                    last_alert.alert_description = "ALERTA DE GIRO BRUSCO"
                    last_alert.alert_priority = trigger.alert_priority
                    last_alert.account = unit.account
                    last_alert.save()
                else:
                    last_alert = LastAlert.objects.create(
                        unit = unit,
                        timestamp = unit.last_timestamp,
                        latitude = unit.last_latitude,
                        longitude = unit.last_longitude,
                        speed = unit.last_speed,
                        angle = unit.last_angle,
                        address = unit.last_address,
                        alert_type = 1011,
                        alert_description = "ALERTA DE GIRO BRUSCO",
                        alert_priority = trigger.alert_priority,
                        account = unit.account
                    )  
                # FIN - ACTUALIZAR ULTIMA ALERTA
                """
    except Exception as e:
        pass