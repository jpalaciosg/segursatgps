from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json
from datetime import datetime
from pytz import timezone

from .models import Device,Group
from .serializers import DeviceSerializer,UpdateDeviceSerializer,GroupSerializer
from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.  
@login_required
def units_view(request):
    # verificar privilegios
    if privilege.view_latest_alerts(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request.user.profile)
    """
    for unit in units:
        try:
            unit.created = unit.created.replace(tzinfo=timezone('America/Lima'))
            unit.modified = unit.modified.replace(tzinfo=timezone('America/Lima'))
        except Exception as e:
            print(e)
    """
    for unit in units:
        unit.odometer = str(unit.odometer)
        unit.modified = gmt_conversor.convert_utctolocaltime(unit.modified).strftime("%d/%m/%Y %H:%M:%S")
        unit.created = gmt_conversor.convert_utctolocaltime(unit.created).strftime("%d/%m/%Y %H:%M:%S")
    return render(request,'units/units.html',{
        'units':units,
    })

@login_required
def unit_group_view(request):
    units = privilege.get_units(request.user.profile)
    groups = Group.objects.filter(account=request.user.profile.account)
    for group in groups:
        group.modified = gmt_conversor.convert_utctolocaltime(group.modified) # convertir a zona horaria
        group.created = gmt_conversor.convert_utctolocaltime(group.created) # convertir a zona horaria
    return render(request,'units/groups.html',{
        'units':units,
        'groups':groups,
    })

@api_view(['GET'])
def get_units(request):
    try:
        units = privilege.get_units(request.user.profile)
        serializer = DeviceSerializer(units,many=True)
        data = serializer.data
        for i in range(len(data)):
            data[i]['modified'] = gmt_conversor.convert_utctolocaltime(units[i].modified).strftime("%d/%m/%Y %H:%M:%S")
            data[i]['created'] = gmt_conversor.convert_utctolocaltime(units[i].created).strftime("%d/%m/%Y %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_unit(request,name):
    try:
        unit = Device.objects.get(name=name)
        serializer = DeviceSerializer(unit,many=False)
        data = serializer.data
        try:
            data['last_attributes'] = json.loads(data['last_attributes'])
        except:
            data['last_attributes'] = ''
        try:
            data['previous_location'] = json.loads(data['previous_location'])
        except:
            data['previous_location'] = ''
        try:
            data['previous_location']['attributes'] = json.loads(data['previous_location']['attributes'])
        except:
            data['previous_location']['attributes'] = ''
        last_report = datetime.fromtimestamp(unit.last_timestamp)
        last_report = gmt_conversor.convert_utctolocaltime(last_report)
        data['last_report'] = last_report.strftime("%d-%m-%Y %H:%M:%S")
        data['modified'] = gmt_conversor.convert_utctolocaltime(unit.modified).strftime("%d/%m/%Y %H:%M:%S")
        data['created'] = gmt_conversor.convert_utctolocaltime(unit.created).strftime("%d/%m/%Y %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_unit_status(request,name):
    unit = Device.objects.get(name=name)
    device_reader = DeviceReader(unit.uniqueid)
    response = device_reader.get_unit_status(unit)
    return Response(response,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_unit(request,id):
    data = request.data
    try:
        unit = Device.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateDeviceSerializer(data=data)
    if serializer.is_valid():
        unit.name = data['unit_name']
        unit.description = data['description']
        unit.odometer = data['odometer']
        unit.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_group(request):
    response = {
        'status': 'OK',
    }
    return Response(response,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_groups(request):
    try:
        groups = Group.objects.filter(account=request.user.profile.account)
        serializer = GroupSerializer(groups,many=True)
        data = serializer.data
        for item in data:
            c_units = item['units']
            item['units'] = []
            for index in c_units:
                try:
                    unit = Device.objects.get(id=index)
                    item['units'].append(unit.name)
                except:
                    pass
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)