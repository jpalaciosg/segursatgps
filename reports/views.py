from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from datetime import datetime,timedelta
import json

from geofences.models import Geofence
from common.time_conversor import TimeConversor
from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor
from common.privilege import Privilege
from common.report import Report

from .forms import ReportForm,MileageReportForm
from .render_report import RenderReport
from units.models import Group

# Create your views here.

gmt_conversor = GMTConversor() #conversor zona horaria
time_conversor = TimeConversor()
privilege = Privilege()
report = Report()
render_report = RenderReport()

@login_required
def dashboard_view(request):
    units = privilege.get_units(request)
    units_transmitting = []
    units_not_transmitted = []
    units_in_motion = []
    units_stopped = []
    now = datetime.now()
    current_timestamp = int(datetime.timestamp(now))

    for unit in units:
        dt = datetime.fromtimestamp(unit.last_timestamp)
        dt = gmt_conversor.convert_utctolocaltime(dt)
        unit.last_report = dt.strftime("%d/%m/%Y %H:%M:%S")
        timeout = current_timestamp - unit.last_timestamp
        if timeout > request.user.profile.account.device_timeout:
            units_not_transmitted.append(unit)
        else:
            units_transmitting.append(unit)
        if unit.last_speed > 0:
            units_in_motion.append(unit)
        else:
            units_stopped.append(unit)

    return render(request,'reports/dashboard.html',{
        'units_transmitting': units_transmitting,
        'units_not_transmitted': units_not_transmitted,
        'units_in_motion': units_in_motion,
        'units_stopped': units_stopped,
        'units': units,
        'now': gmt_conversor.convert_utctolocaltime(now),
    })

@login_required
def fleet_status_view(request):
    units = privilege.get_units(request)
    now = datetime.now()
    current_timestamp = int(datetime.timestamp(now))
    units_not_transmitted = 0
    units_in_motion = 0
    units_stopped = 0
    for unit in units:
        unit.odometer = round(unit.odometer,1)
        dt = datetime.fromtimestamp(unit.last_timestamp)
        dt = gmt_conversor.convert_utctolocaltime(dt)
        unit.last_report = dt.strftime("%d/%m/%Y %H:%M:%S")
        unit.last_report_date = dt.strftime("%Y/%m/%d %H:%M:%S").split(" ")[0]
        unit.last_report_time = dt.strftime("%Y/%m/%d %H:%M:%S").split(" ")[1]
        ## sumarizar totales
        timeout = current_timestamp - unit.last_timestamp
        if timeout > request.user.profile.account.device_timeout:
            units_not_transmitted += 1
        if unit.last_speed > 0:
            units_in_motion += 1
        else:
            units_stopped += 1
        unit.timeout = int(timeout)
        device_reader = DeviceReader(unit.uniqueid)
        unit.last_ignition = device_reader.detect_ignition_event({
            'attributes':json.loads(unit.last_attributes)
        })
        c_time = device_reader.get_hours({
            'attributes':json.loads(unit.last_attributes)
        })
        hours = int(c_time/3600)
        minutes = int(c_time%3600/60)
        unit.last_hours = f"{hours} h {minutes} m"
        try:
            current_power = json.loads(unit.last_attributes)['power']
        except:
            current_power = 0
        if current_power > 10:
            unit.main_battery = True
            unit.secondary_battery = True
        else:
            unit.main_battery = False
            unit.secondary_battery = True
    units_transmitting = len(units) - units_not_transmitted
    return render(request,'reports/fleet-status.html',{
        'units': units,
        'now': gmt_conversor.convert_utctolocaltime(now),
        'units_transmitting': str(units_transmitting),
        'units_not_transmitted': units_not_transmitted,
        'units_in_motion': units_in_motion,
        'units_stopped': units_stopped,
    })

@api_view(['POST'])
def get_detailed_report(request):
    return render_report.render_detailed_report(request)

@login_required
def detailed_report_view(request):
    # verificar privilegios
    if privilege.view_detailed_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/detailed-report.html',{
        'units':units,
    })

@login_required
def detailed_report_with_attributes_view(request):
    # verificar privilegios
    if privilege.view_detailed_report_with_attributes(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/detailed-report-with-attributes.html',{
        'units':units,
    })

@api_view(['POST'])
def get_driving_style_report(request):
    return render_report.render_driving_style_report(request)

def driving_style_report_view(request):
    # verificar privilegios
    if privilege.view_driving_style_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/driving-style-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_trip_report1(request):
    return render_report.render_trip_report1(request)

@api_view(['POST'])
def get_trip_report2(request):
    return render_report.render_trip_report2(request)

@login_required
def trip_report_view(request):
    # verificar privilegios
    if privilege.view_trip_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    units = privilege.get_units(request)
    return render(request,'reports/trip-report.html',{
        'units':units,
    })

@login_required
def trip_report2_view(request):
    # verificar privilegios
    if privilege.view_day_trip_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/trip-report2.html',{
        'units':units,
    })

@login_required
def group_trip_report_view(request):
    # verificar privilegios
    if privilege.view_group_trip_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-trip-report.html',{
        'groups':groups,
    })

@api_view(['POST'])
def get_stop_report(request):
    return render_report.render_stop_report(request)

@login_required
def stop_report_view(request):
    # verificar privilegios
    if privilege.view_stop_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    units = privilege.get_units(request)
    return render(request,'reports/stop-report.html',{
        'units':units,
    })

# GROUP STOP REPORT
@login_required
def group_stop_report_view(request):
    # verificar privilegios
    if privilege.view_group_stop_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-stop-report.html',{
        'groups':groups,
    })

# REPORTE DE VELOCIDAD
@api_view(['POST'])
def get_speed_report(request):
    return render_report.render_speed_report(request)

@login_required
def speed_report_view(request):
    # verificar privilegios
    if privilege.view_speed_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/speed-report.html',{
        'units':units,
    })

# GROUP SPEED REPORT
@login_required
def group_speed_report_view(request):
    # verificar privilegios
    if privilege.view_group_speed_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-speed-report.html',{
        'groups':groups,
    })

@api_view(['POST'])
def get_mileage_report(request):
    return render_report.render_mileage_report(request)

# MILEAGE REPORT
@login_required
def mileage_report_view(request):
    # verificar privilegios
    if privilege.view_mileage_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    #GET
    units = privilege.get_units(request)
    form = MileageReportForm()
    return render(request,'reports/mileage-report.html',{
        'units':units,
        'form':form,
    })

# GROUP MILEAGE REPORT
@login_required
def group_mileage_report_view(request):
    if privilege.view_group_mileage_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-mileage-report.html',{
        'groups':groups,
    })

# GEOFENCE REPORT
@login_required
def geofence_report_view(request):
    # verificar privilegios
    if privilege.view_geofence_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    #GET
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    units = privilege.get_units(request)
    form = ReportForm()
    return render(request,'reports/geofence-report.html',{
        'units':units,
        'geofences':geofences,
        'form':form,
    })

@api_view(['POST'])
def get_geofence_report(request):
    return render_report.render_geofence_report(request)

# GROUP GEOFENCE REPORT
@login_required
def group_geofence_report_view(request):
    # verificar privilegios
    if privilege.view_geofence_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    # GET
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    groups = Group.objects.filter(account=request.user.profile.account)
    return render(request,'reports/group-geofence-report.html',{
        'groups':groups,
        'geofences':geofences,
    })

@login_required
def telemetry_report_view(request):
    # verificar privilegios
    if privilege.view_telemetry_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/telemetry-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_telemetry_report(request):
    return render_report.render_telemetry_report(request)

@login_required
def temperature_report_view(request):
    # verificar privilegios
    if privilege.view_temperature_report(request) == False:
        return HttpResponse("<h1>Acceso Restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/temperature-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_temperature_report(request):
    return render_report.render_temperature_report(request)

@login_required
def hours_report_view(request):
    #GET
    # verificar privilegios
    if privilege.view_hours_report(request) == False:
        return HttpResponse("<h1>Acceso Restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
    return render(request,'reports/hours-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_hours_report(request):
    return render_report.render_hours_report(request)

@login_required
def telemetry_trip_report_view(request):
    units = privilege.get_units(request)
    return render(request,'reports/telemetry-trip-report.html',{
        'units':units,
    })

@login_required
def target_telemetry_report_view(request):
    units = privilege.get_units(request)
    return render(request,'reports/target-telemetry-report.html',{
        'units':units,
    })

@api_view(['POST'])
def get_target_telemetry_report(request):
    pass

@api_view(['POST'])
def get_group_driving_style_report(request):
    return render_report.render_group_driving_style_report(request)

def group_driving_style_report_view(request):
    # verificar privilegios
    if privilege.view_driving_style_report(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    groups = privilege.get_groups(request)
    return render(request,'reports/driving-style-report.html',{
        'groups':groups,
    })