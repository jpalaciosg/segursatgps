import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

from datetime import datetime,timedelta

from common.gmt_conversor import GMTConversor

from units.serializers import DeviceSerializer
from units.models import Device,Group

gmt_conversor = GMTConversor()

# Create your views here.
@api_view(['GET'])
def get_all_units(request):
    units = Device.objects.all()
    now = datetime.now()
    current_timestamp = int(datetime.timestamp(now))
    serializer = DeviceSerializer(units,many=True)
    data = serializer.data
    for item in data:
        item['odometer'] = round(item['odometer'],1)
        dt = datetime.fromtimestamp(item['last_timestamp'])
        dt = gmt_conversor.convert_utctolocaltime(dt)
        item['last_report'] = dt.strftime("%d/%m/%Y %H:%M:%S")
        item['timeout'] = current_timestamp - item['last_timestamp']
        item['last_attributes'] = json.loads(item['last_attributes'])
        item['previous_location'] = json.loads(item['previous_location'])
    return Response(data,status=status.HTTP_200_OK)

@login_required
def management_map_view(request):
    return render(request,'management/map.html')

@login_required
def management_dashboard_view(request):
    units = Device.objects.all()
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
    return render(request,'management/dashboard.html',{
        'units_transmitting': units_transmitting,
        'units_not_transmitted': units_not_transmitted,
        'units_in_motion': units_in_motion,
        'units_stopped': units_stopped,
        'units': units,
        'now': gmt_conversor.convert_utctolocaltime(now),
    })

@login_required
def management_view(request):
    return render(request,'management/main.html')