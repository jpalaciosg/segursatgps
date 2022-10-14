from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from datetime import datetime,timedelta
import requests
from requests.auth import HTTPBasicAuth
import json

from common.gmt_conversor import GMTConversor

from units.models import Device
from users.models import Account,Profile, User
from .serializers import AccountSerializer,DeviceSerializer,UserSerializer,EditUserSerializer,ProfileSerializer,UpdateProfileSerializer,UpdatePasswordSerializer

gmt_conversor = GMTConversor()

# Create your views here.
@login_required
def management_map_view(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    return render(request,'management/map.html')

@login_required
def management_dashboard_view(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
        if timeout > unit.account.device_timeout:
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    return render(request,'management/accounts.html')

@api_view(['GET'])
def get_account(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    accounts = Account.objects.all()
    return render(request,'management/users.html',{
        'accounts':accounts
    })

@api_view(['GET'])
def get_users(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    accountid = request.GET.get('accountid',None)
    profiles = None
    if accountid:
        try:
            accountid = int(accountid)
            account = Account.objects.get(id=accountid)
            profiles = Profile.objects.filter(account=account)
        except:
            profiles = []
    else:
        profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles,many=True)
    data = serializer.data
    for i in range(len(data)):
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(profiles[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(profiles[i].modified).strftime("%d/%m/%Y %H:%M:%S")
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    try:
        profile = Profile.objects.get(id=id)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(profile,many=False)
    data = serializer.data
    return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    data = request.data
    if 'is_superuser' in data.keys() or 'is_staff' in data.keys():
        error = {
            'detail': "Te crees pendejo!"
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    if 'account' in data.keys():
        try:
            account = Account.objects.get(id=data['account'])
        except Exception as e:
            error = {'errors':{
                'account': "This account does not exist."
            }}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    else:
        error = {'errors':{
            'account': "This field is required."
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    if 'password' in data.keys():
        data['password'] = make_password(data['password'])
    user_serializer = UserSerializer(data=data)
    if user_serializer.is_valid():
        user_serializer.create(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':user_serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    data = request.data
    try:
        profile = Profile.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': 'Username does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = EditUserSerializer(data=data)
    if serializer.is_valid():
        profile.user.description = data['description']
        profile.user.email = data['email']
        profile.user.is_active = data['is_active']
        profile.user.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

#DELETE USER BY ID
@api_view(['DELETE'])
def delete_user(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    try:
        profile = Profile.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'name': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    profile.delete()
    response = {
        'status': 'OK',
        'description': 'The user was deleted successfully.'
    }
    return Response(response,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_profile(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    data = request.data
    try:
        profile = Profile.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': 'User does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateProfileSerializer(profile,data=data)
    if serializer.is_valid():
        try:
            account = Account.objects.get(id=data['account'])
        except:
            error = {
                'detail': 'Account does not exist.'
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        profile.account = account
        profile.is_admin = data['is_admin']
        profile.view_detailed_report = data['view_detailed_report']
        profile.view_speed_report = data['view_speed_report']
        profile.view_stop_report = data['view_stop_report']
        profile.view_trip_report = data['view_trip_report']
        profile.view_day_trip_report = data['view_day_trip_report']
        profile.view_mileage_report = data['view_mileage_report']
        profile.view_geofence_report = data['view_geofence_report']
        profile.view_driving_style_report = data['view_driving_style_report']
        profile.view_telemetry_report = data['view_telemetry_report']
        profile.view_hours_report = data['view_hours_report']
        profile.view_temperature_report = data['view_temperature_report']
        profile.view_detailed_report_with_attributes = data['view_detailed_report_with_attributes']
        profile.view_group_trip_report = data['view_group_trip_report']
        profile.view_group_speed_report = data['view_group_speed_report']
        profile.view_group_mileage_report = data['view_group_mileage_report']
        profile.view_group_stop_report = data['view_group_stop_report']
        profile.view_group_geofence_report = data['view_group_geofence_report']
        profile.view_latest_alerts = data['view_latest_alerts']
        profile.view_alert_history = data['view_alert_history']
        profile.view_units = data['view_units']
        #Eslim
        profile.view_units_group = data['view_units_group']
        #Eslim
        profile.view_unit_triggers = data['view_unit_triggers']
        profile.view_fleet_triggers = data['view_fleet_triggers']
        profile.view_mail_lists = data['view_mail_lists']
        profile.view_geofences = data['view_geofences']
        #Eslim
        profile.view_geofences_group = data['view_geofences_group']
        #Eslim
        profile.view_users = data['view_users']
        profile.units.clear()
        for id in data['units']:
            try:
                device = Device.objects.get(id=id)
                profile.units.add(device)
            except Exception as e:
                pass
        profile.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_password(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    data = request.data
    try:
        profile = Profile.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': 'User does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdatePasswordSerializer(data=data)
    if serializer.is_valid():
        if data['password'] == data['password_confirmation']:
            profile.user.password = make_password(data['password'])
            profile.user.save()
            response = {
                'status': 'OK',
                'description': 'Password has been changed.',
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {
                'status': 'ERROR',
                'description': 'The password has not been changed.',
            }
    else:
        response = {
            'status': 'ERROR',
            'description': 'The password has not been changed.',
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

@login_required
def units_view(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    accounts = Account.objects.all()
    return render(request,'management/units.html',{
        'accounts':accounts
    })

@api_view(['GET'])
def get_units(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    accountid = request.GET.get('accountid',None)
    units = None
    if accountid:
        try:
            accountid = int(accountid)
            account = Account.objects.get(id=accountid)
            units = Device.objects.filter(account=account)
        except:
            units = []
    else:
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
        data[i]['account_name'] = units[i].account.name
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_units_from_account(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    try:
        account = Account.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': 'Account does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    units = Device.objects.filter(account=account)
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
        data[i]['account_name'] = units[i].account.name
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_unit(request,id):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
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
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    #data = request.data
    try:
        unit = Device.objects.get(id=id)
    except Exception as e:
        error = {'errors':{
            'id': str(e)
        }}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    unit.delete()
    response = {
        'status': 'OK',
        'description': 'Unit was deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)

@login_required
def management_view(request):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    return render(request,'management/main.html')

@api_view(['GET'])
def get_traccar_unit(request,uniqueid):
    # verificar privilegios
    if request.user.profile.is_superadmin == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    try:
        URL = f"http://gps.segursat.com:8082/api/devices?uniqueId={uniqueid}"
        USER = 'admin'
        PASSWORD = 'Conejo123$$'
        auth = HTTPBasicAuth(USER, PASSWORD)
        headers = {
        'Content-Type': 'application/json; charset=utf-8',
        }
        response = requests.get(URL,headers=headers,auth=auth)
        return Response(response.json(),status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
