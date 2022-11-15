from units.models import Device,Group

class Privilege:

    def get_units(self,request):
        is_admin = request.user.profile.is_admin
        units = None
        if is_admin:
            units = Device.objects.filter(account=request.user.profile.account)
        else:
            units = request.user.profile.units.all()
        # CAMBIO PROVISIONAL SOLGAS
        if request.user.profile.account.name == '20100176450':
            if request.path.find('reports') != -1:
                if units:
                    for unit in units:
                        try:
                            parent = Device.objects.get(child__id=unit.id)
                            unit.id = parent.id
                        except Exception as e:
                            pass
        # FIN - CAMBIO PROVISIONAL SOLGAS
        return units

    def get_groups(self,request):
        groups = Group.objects.filter(account=request.user.profile.account)
        return groups

    def view_detailed_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_detailed_report == False:
                return False
        return True

    def view_speed_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_speed_report == False:
                return False
        return True

    def view_stop_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_stop_report == False:
                return False
        return True

    def view_trip_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_trip_report == False:
                return False
        return True

    def view_day_trip_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_day_trip_report == False:
                return False
        return True

    def view_mileage_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_mileage_report == False:
                return False
        return True

    def view_geofence_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_geofence_report == False:
                return False
        return True

    def view_driving_style_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_driving_style_report == False:
                return False
        return True

    def view_telemetry_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_telemetry_report == False:
                return False
        return True

    def view_detailed_report_with_attributes(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_detailed_report_with_attributes == False:
                return False
        return True

    def view_group_trip_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_group_trip_report == False:
                return False
        return True

    def view_group_stop_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_group_stop_report == False:
                return False
        return True

    def view_group_mileage_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_group_mileage_report == False:
                return False
        return True

    def view_group_speed_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_group_speed_report == False:
                return False
        return True

    def view_group_geofence_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_group_geofence_report == False:
                return False
        return True

    def view_units(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_units == False:
                return False
        return True

    #Eslim
    def view_units_group(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_units_group == False:
                return False
        return True
    #Eslim

    def view_unit_triggers(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_unit_triggers == False:
                return False
        return True

    def view_fleet_triggers(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_fleet_triggers == False:
                return False
        return True

    def view_mail_lists(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_mail_lists == False:
                return False
        return True

    def view_geofences(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_geofences == False:
                return False
        return True

    #Eslim
    def view_geofences_group(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_geofences_group == False:
                return False
        return True
    #Eslim

    def view_users(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_users == False:
                return False
        return True

    def view_latest_alerts(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_latest_alerts == False:
                return False
        return True

    def view_alert_history(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_alert_history == False:
                return False
        return True

    def view_hours_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_hours_report == False:
                return False
        return True

    def view_temperature_report(self,request):
        if request.user.profile.is_admin == False:
            if request.user.profile.view_temperature_report == False:
                return False
        return True