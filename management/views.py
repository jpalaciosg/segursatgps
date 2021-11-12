from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

from datetime import datetime

from common.gmt_conversor import GMTConversor

from units.serializers import DeviceSerializer
from units.models import Device,Group

gmt_conversor = GMTConversor()

# Create your views here.
@api_view(['GET'])
def get_complete_fleet_status(request):
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
    return Response(data,status=status.HTTP_200_OK)

