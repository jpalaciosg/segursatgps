import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

from datetime import datetime,timedelta

from common.gmt_conversor import GMTConversor

from units.models import Device
from units.serializers import DeviceSerializer
from users.models import Account
from users.serializers import AccountSerializer

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
def accounts_view(request):
    accounts = Account.objects.all()
    return render(request,'management/accounts.html',{
        'accounts': accounts,
    })

@api_view(['GET'])
def get_account(request,name):
    try:
        account = Account.objects.get(name=name)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = AccountSerializer(account,many=False)
    data = serializer.data
    data['created'] = gmt_conversor.convert_utctolocaltime(account.created).strftime("%d/%m/%Y %H:%M:%S")
    data['modified'] = gmt_conversor.convert_utctolocaltime(account.modified).strftime("%d/%m/%Y %H:%M:%S")
    #data['device_timeout'] = str(timedelta(seconds=data['device_timeout']))
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts,many=True)
    data = serializer.data
    for i in range(len(data)):
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(accounts[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(accounts[i].modified).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['device_timeout'] = str(timedelta(seconds=data[i]['device_timeout']))
    return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_account(request):
    data = request.data
    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response = {
            'status':'OK'
        }
        Response(response,status=status.HTTP_200_OK)
    else:
        Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete_account(request,name):
    try:
        account = Account.objects.get(name=name)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    response = {
        'status': 'OK',
        'description': 'The account was deleted successfully.'
    }
    return Response(response,status=status.HTTP_200_OK)

@login_required
def management_view(request):
    return render(request,'management/main.html')

