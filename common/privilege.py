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
    
    def view_detailed_report(self,profile):
        if profile.is_admin == False:
            if profile.view_detailed_report == False:
                return False
        return True

    def view_speed_report(self,profile):
        if profile.is_admin == False:
            if profile.view_speed_report == False:
                return False
        return True

    def view_stop_report(self,profile):
        if profile.is_admin == False:
            if profile.view_stop_report == False:
                return False
        return True

    def view_trip_report(self,profile):
        if profile.is_admin == False:
            if profile.view_trip_report == False:
                return False
        return True

    def view_mileage_report(self,profile):
        if profile.is_admin == False:
            if profile.view_mileage_report == False:
                return False
        return True

    def view_geofence_report(self,profile):
        if profile.is_admin == False:
            if profile.view_geofence_report == False:
                return False
        return True

    def view_driving_style_report(self,profile):
        if profile.is_admin == False:
            if profile.view_driving_style_report == False:
                return False
        return True

    def view_telemetry_report(self,profile):
        if profile.is_admin == False:
            if profile.view_telemetry_report == False:
                return False
        return True