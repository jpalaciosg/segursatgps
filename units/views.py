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
from .serializers import DeviceSerializer,UpdateDeviceSerializer,GroupSerializer,UpdateGroupSerializer
from common.device_reader import DeviceReader
from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@login_required
def units_view(request):
    # verificar privilegios
    if privilege.view_latest_alerts(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = privilege.get_units(request)
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
    units = privilege.get_units(request)
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
        units = privilege.get_units(request)
        serializer = DeviceSerializer(units,many=True)
        data = serializer.data
        for i in range(len(data)):
            last_report = gmt_conversor.convert_utctolocaltime(
                datetime.utcfromtimestamp(data[i]['last_timestamp']))
            data[i]['last_report'] = last_report.strftime("%d/%m/%Y, %H:%M:%S")
            data[i]['modified'] = gmt_conversor.convert_utctolocaltime(units[i].modified).strftime("%d/%m/%Y %H:%M:%S")
            data[i]['created'] = gmt_conversor.convert_utctolocaltime(units[i].created).strftime("%d/%m/%Y %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_unit(request,name):
    try:
        unit = Device.objects.get(name=name,account=request.user.profile.account)
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
        data['last_report'] = last_report.strftime("%d-%m-%Y, %H:%M:%S")
        data['modified'] = gmt_conversor.convert_utctolocaltime(unit.modified).strftime("%d/%m/%Y %H:%M:%S")
        data['created'] = gmt_conversor.convert_utctolocaltime(unit.created).strftime("%d/%m/%Y %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_unit_status(request,id):
    unit = Device.objects.get(id=id)
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
        unit.show_unit_name_in_map = data['show_unit_name_in_map']
        unit.show_unit_description_in_map = data['show_unit_description_in_map']
        unit.show_unit_datetime_in_map = data['show_unit_datetime_in_map']
        try:
            unit.save()
        except Exception as e:
            error = {
                'detail': str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_group(request):
    data = request.data
    data['account'] = request.user.profile.account.id
    serializer = GroupSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)


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
                    unit_serializer = DeviceSerializer(unit,many=False)
                    unit_data = unit_serializer.data
                    try:
                        unit_data['last_attributes'] = json.loads(unit_data['last_attributes'])
                    except:
                        unit_data['last_attributes'] = ''
                    try:
                        unit_data['previous_location'] = json.loads(unit_data['previous_location'])
                    except:
                        unit_data['previous_location'] = ''
                    try:
                        unit_data['previous_location']['attributes'] = json.loads(unit_data['previous_location']['attributes'])
                    except:
                        unit_data['previous_location']['attributes'] = ''
                    last_report = datetime.fromtimestamp(unit.last_timestamp)
                    last_report = gmt_conversor.convert_utctolocaltime(last_report)
                    unit_data['last_report'] = last_report.strftime("%d-%m-%Y, %H:%M:%S")
                    item['units'].append(unit_data)
                except Exception as e:
                    pass
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_group(request,id):
    try:
        group = Group.objects.get(id=id,account=request.user.profile.account)
        serializer = GroupSerializer(group,many=False)
        data = serializer.data
        c_units = data['units']
        data['units'] = []
        for index in c_units:
            try:
                unit = Device.objects.get(id=index)
                unit_serializer = DeviceSerializer(unit,many=False)
                unit_data = unit_serializer.data
                try:
                    unit_data['last_attributes'] = json.loads(unit_data['last_attributes'])
                except:
                    unit_data['last_attributes'] = ''
                try:
                    unit_data['previous_location'] = json.loads(unit_data['previous_location'])
                except:
                    unit_data['previous_location'] = ''
                try:
                    unit_data['previous_location']['attributes'] = json.loads(unit_data['previous_location']['attributes'])
                except:
                    unit_data['previous_location']['attributes'] = ''
                last_report = datetime.fromtimestamp(unit.last_timestamp)
                last_report = gmt_conversor.convert_utctolocaltime(last_report)
                unit_data['last_report'] = last_report.strftime("%d-%m-%Y, %H:%M:%S")
                data['units'].append(unit_data)
            except:
                pass
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_group(request,id):
    data = request.data
    try:
        group = Group.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateGroupSerializer(data=data)
    if serializer.is_valid():
        group.name = data['name']
        group.description = data['description']
        group.units.clear()
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                group.units.add(device)
            except:
                pass
        group.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_group(request,id):
    try:
        group = Group.objects.get(id=id,account=request.user.profile.account)
    except Exception as e:
        error = {'errors':{
            'id': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    group.delete()
    response = {
        'status': 'OK',
        'description': 'Group was deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)