from async_timeout import current_task
from triggers.models import FleetTrigger
from units.models import Device
from alerts.models import Alert,LastAlert
from units.models import LastAlert
from datetime import datetime

fleet_triggers = FleetTrigger.objects.filter(alert_type=1012)

for trigger in fleet_triggers:
    try:
        units = Device.objects.filter(account=trigger.account)
        seconds = trigger.extension1012.seconds
        for unit in units:
            current_timestamp = int(datetime.now().timestamp())
            offset = current_timestamp - unit.last_timestamp
            if offset > seconds:
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
                    last_alert.alert_type = 1012
                    last_alert.alert_description = "ALERTA DE FALLA DE TRANSMISION"
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
                        alert_type = 1012,
                        alert_description = "ALERTA DE FALLA DE TRANSMISION",
                        alert_priority = trigger.alert_priority,
                        account = unit.account
                    )
                # FIN - ACTUALIZAR ULTIMA ALERTA
                alert = Alert.objects.create(
                    unitid = unit.id,
                    timestamp = unit.last_timestamp,
                    latitude = unit.last_latitude,
                    longitude = unit.last_longitude,
                    speed = unit.last_speed,
                    angle = unit.last_angle,
                    address = unit.last_address,
                    alert_type = 1012,
                    alert_description = "ALERTA DE FALLA DE TRANSMISION",
                    alert_priority = trigger.alert_priority,
                    reference = unit.name,
                    accountid = unit.account.id
                )
                dt = datetime.fromtimestamp(alert.timestamp)
                dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                dt = dt.strftime("%d/%m/%Y %H:%M:%S")
                channel_layer = channels.layers.get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    f'chat_{unit.account.name}',
                    {
                        'type': 'send_message',
                        'message': {
                            'type':'update_alert',
                            'payload': {
                                'unit_id': unit.id,
                                'unit_name': unit.name,
                                'unit_description': unit.description,
                                'timestamp': alert.timestamp,
                                'datetime': dt,
                                'latitude': alert.latitude,
                                'longitude': alert.longitude,
                                'speed': alert.speed,
                                'angle': alert.angle,
                                'address': alert.address,
                                'alert_type': alert.alert_type,
                                'alert_description': alert.alert_description,
                                'alert_priority': alert.alert_priority,
                                'alert_id': alert.id
                            }
                        }
                    }
                )
                if trigger.send_notification:
                    async_to_sync(channel_layer.group_send)(
                        f'chat_{unit.account.name}',
                        {
                            'type': 'send_message',
                            'message': {
                                'type':'notification',
                                'payload': {
                                    'title': f'{unit.name} - {unit.description}',
                                    'message': alert.alert_description,
                                }
                            }
                        }
                    )
                if trigger.send_mail_notification and trigger.mail_list:
                    AlertMailQueue.objects.create(
                        alert_description = alert.alert_description,
                        alert_timestamp = alert.timestamp,
                        alert_latitude = alert.latitude,
                        alert_longitude = alert.longitude,
                        alert_speed = alert.speed,
                        alert_angle = alert.angle,
                        alert_address = alert.address,
                        unit_name = unit.name,
                        unit_description = unit.description,
                        account_id = unit.account.id,
                        customer_description = unit.account.description,
                        mails = trigger.mail_list.mails,
                    )
    except Exception as e:
        print(e)