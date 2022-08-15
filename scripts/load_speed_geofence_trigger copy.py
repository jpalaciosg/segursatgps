from triggers.models import FleetTrigger,FleetTriggerExtension1006
from geofences.models import Geofence
from users.models import Account

account = Account.objects.get(name='civa')
geofences = Geofence.objects.filter(account=account,description__startswith='10')

for geofence in geofences:
    print(geofence.name)
    print(geofence.description)

trigger = FleetTrigger.objects.create(
    name = "EXCESO DE VELOCIDAD POR GEOCERCA - 10KM/H",
    description = "10KM//H",
    alert_type = 1006,
    is_active = True,
    send_notification = True,
    send_mail_notification = True,
    account = account
)

extension1006 = FleetTriggerExtension1006.objects.create(
    speed = 10,
    account = account
)
extension1006.geofences.set(geofences)
extension1006.save()

trigger.extension1006 = extension1006
trigger.save()
