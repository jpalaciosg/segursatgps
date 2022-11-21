from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from users.models import User
from units.models import Device
from .models import Profile
from .forms import UserCreateForm,UserUpdateForm
from .serializers import ProfileSerializer,UserSerializer,UpdateUserSerializer,UpdateProfileSerializer,UpdatePasswordSerializer

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mode = request.POST['mode']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            try:
                profile = request.user.profile
            except:
                profile = None
            if profile:
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                else:
                    if mode == '0':
                        return redirect('map')
                    elif mode == '1':
                        return redirect('main')
                    else:
                        return redirect('map')
            logout(request)
            return render(request,'users/login.html',{
                'error':'No existe cuenta vinculada a este usuario, contactese con el administrador',
            })
        else:
            return render(request,'users/login.html',{'error':'Usuario y/o contraseña invalidos'})
    return render(request,'users/login.html')

def superadmin_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if request.user.profile.is_superadmin:
                return redirect('management-dashboard')
            logout(request)
            return render(request,'users/salogin.html',{
                'error':'No cuenta con los privilegios necesarios.',
            })
        else:
            return render(request,'users/salogin.html',{'error':'Usuario y/o contraseña invalidos'})

    return render(request,'users/salogin.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def users_view(request):
    # GET
    profiles = Profile.objects.filter(account=request.user.profile.account)
    for profile in profiles:
        try:
            #profile.user.last_login = profile.user.last_login.replace(tzinfo=timezone('America/Lima'))
            profile.user.last_login = gmt_conversor.convert_localtimetoutc(profile.user.last_login).strftime("%d/%m/%Y %H:%M:%S")
        except Exception as e:
            print(e)
        profile.modified = gmt_conversor.convert_localtimetoutc(profile.modified).strftime("%d/%m/%Y %H:%M:%S")
        profile.created = gmt_conversor.convert_localtimetoutc(profile.created).strftime("%d/%m/%Y %H:%M:%S")
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    return render(request,'users/users.html',{
        'profiles':profiles,
        'navbar':navbar,
    })

@api_view(['GET'])
def get_users(request):
    profiles = Profile.objects.filter(account=request.user.profile.account)
    serializer = ProfileSerializer(profiles,many=True)
    data = serializer.data
    for i in range(len(data)):
        data[i]['created'] = gmt_conversor.convert_utctolocaltime(profiles[i].created).strftime("%d/%m/%Y %H:%M:%S")
        data[i]['modified'] = gmt_conversor.convert_utctolocaltime(profiles[i].modified).strftime("%d/%m/%Y %H:%M:%S")
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request,id):
    try:
        profile = Profile.objects.get(id=id,account=request.user.profile.account)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(profile,many=False)
    data = serializer.data
    return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    data = request.data
    if 'is_superuser' in data or 'is_staff' in data:
        error = {
            'detail': "Te crees pendejo!"
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    if 'password' in data:
        data['password'] = make_password(data['password'])
    user_serializer = UserSerializer(data=data)
    if user_serializer.is_valid():
        user_serializer.create(data,request)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':user_serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request,id):
    data = request.data
    try:
        profile = Profile.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': 'Profile does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateUserSerializer(data=data)
    if serializer.is_valid():
        profile.user.description = data['description']
        profile.user.email = data['email']
        profile.user.is_active = data['is_active']
        profile.user.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_password(request,id):
    data = request.data
    try:
        profile = Profile.objects.get(id=id,account=request.user.profile.account)
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

#By Eslim
@api_view(['DELETE'])
def delete_user(request,id):
    try:
        profile = Profile.objects.get(id=id,account=request.user.profile.account)
    except Exception as e:
        error = {
            'detail': 'User does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    profile.user.delete()
    profile.delete()
    response = {
        'status': 'OK',
        'description': 'User has been deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)
#By Eslim

@api_view(['PUT'])
def update_profile(request,id):
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
        profile.view_geofences = data['view_geofences']
        #Eslim
        profile.view_geofences_group = data['view_geofences_group']
        #Eslim
        profile.view_unit_triggers = data['view_unit_triggers']
        profile.view_fleet_triggers = data['view_fleet_triggers']
        profile.view_mail_lists = data['view_mail_lists']
        profile.view_users = data['view_users']
        profile.units.clear()
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                profile.units.add(device)
            except:
                pass
        profile.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_basic_current_user_information(request):
    data = {
        'username': request.user.username,
        'description': request.user.description,
        'account_name': request.user.profile.account.name,
        'account_description': request.user.profile.account.description,
    }
    return Response(data,status=status.HTTP_200_OK)
