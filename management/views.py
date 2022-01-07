import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

from datetime import datetime,timedelta

from common.gmt_conversor import GMTConversor

from units.models import Device
from users.models import Account,Profile
from users.serializers import ProfileSerializer
from .serializers import AccountSerializer,DeviceSerializer,UserSerializer

gmt_conversor = GMTConversor()

# Create your views here.
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
def accounts_view(request):
    return render(request,'management/accounts.html')

@api_view(['GET'])
def get_account(request,id):
    try:
        account = Account.objects.get(id=id)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = AccountSerializer(account,many=False)
    data = serializer.data
    data['created'] = gmt_conversor.convert_utctolocaltime(account.created).strftime("%d/%m/%Y %H:%M:%S")
    data['modified'] = gmt_conversor.convert_utctolocaltime(account.modified).strftime("%d/%m/%Y %H:%M:%S")
    data['timedelta_device_timeouT'] = str(timedelta(seconds=data['device_timeout']))
    return Response(data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_account(request,id):
    data = request.data
    try:
        account = Account.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'name': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = AccountSerializer(account,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_account(request,id):
    data = request.data
    try:
        account = Account.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'name': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #account.delete()
    response = {
        'status': 'OK',
        'description': 'Account was deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts,many=True)
    data = serializer.data
    for i in range(len(data)):
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(accounts[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(accounts[i].modified).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['timedelta_device_timeout'] = str(timedelta(seconds=data[i]['device_timeout']))
    return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_account(request):
    data = request.data
    serializer = AccountSerializer(data=data)
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
def delete_account(request,id):
    try:
        account = Account.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'name': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #account.delete()
    response = {
        'status': 'OK',
        'description': 'The account was deleted successfully.'
    }
    return Response(response,status=status.HTTP_200_OK)

@login_required
def users_view(request):
    return render(request,'management/users.html')

@api_view(['GET'])
def get_users(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles,many=True)
    data = serializer.data
    for i in range(len(data)):
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(profiles[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(profiles[i].modified).strftime("%d/%m/%Y %H:%M:%S")
    return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def units_view(request):
    return render(request,'management/units.html')

@api_view(['GET'])
def get_units(request):
    units = Device.objects.all()
    now = datetime.now()
    current_timestamp = int(datetime.timestamp(now))
    serializer = DeviceSerializer(units,many=True)
    data = serializer.data    
    for i in range(len(data)):
        data[i]['odometer'] = round(data[i]['odometer'],1)
        dt = datetime.fromtimestamp(data[i]['last_timestamp'])
        dt = gmt_conversor.convert_utctolocaltime(dt)
        data[i]['last_report'] = dt.strftime("%d/%m/%Y %H:%M:%S")
        data[i]['timeout'] = current_timestamp - data[i]['last_timestamp']
        data[i]['last_attributes'] = json.loads(data[i]['last_attributes'])
        data[i]['previous_location'] = json.loads(data[i]['previous_location'])
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(units[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(units[i].modified).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['timeout'] = str(timedelta(seconds=data[i]['timeout']))
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_unit(request,id):
    try:
        unit = Device.objects.get(id=id)
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
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_unit(request):
    data = request.data
    serializer = DeviceSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_unit(request,id):
    data = request.data
    try:
        unit = Device.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'id': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = DeviceSerializer(unit,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_unit(request,id):
    data = request.data
    try:
        unit = Device.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'id': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #unit.delete()
    response = {
        'status': 'OK',
        'description': 'Unit was deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)

@login_required
def management_view(request):
    return render(request,'management/main.html')

