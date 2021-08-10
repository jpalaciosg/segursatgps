from units.models import Device 

class Privilege:
    def get_units(self,profile):
        is_admin = profile.is_admin
        units = None
        if is_admin:
            units = Device.objects.filter(account=profile.account)
        else:
            units = profile.units.all()
        return units

