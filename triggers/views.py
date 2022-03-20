from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from triggers.serializers import FleetTriggerSerializer,UpdateFleetTriggerSerializer,FleetTrigger1003Serializer

from .models import FleetTrigger,FleetTriggerExtension1003
from mails.models import MailList
from geofences.models import Geofence

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@login_required
def fleet_trigger_view(request):
    # verificar privilegios
    if privilege.view_latest_alerts(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    triggers = FleetTrigger.objects.filter(account=request.user.profile.account)
    mail_lists = MailList.objects.filter(account=request.user.profile.account)
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    for trigger in triggers:
        try:
            trigger.created = gmt_conversor.convert_utctolocaltime(trigger.created)
            trigger.modified = gmt_conversor.convert_utctolocaltime(trigger.modified)
        except Exception as e:
            print(e)
    return render(request,'triggers/fleet-trigger.html',{
        'triggers':triggers,
        'mail_lists':mail_lists,
        'geofences': geofences,
    })

@api_view(['GET'])
def get_fleet_triggers(request):
    try:
        triggers = FleetTrigger.objects.filter(account=request.user.profile.account)
        serializer = FleetTriggerSerializer(triggers,many=True)
        data = serializer.data
        for i in range(len(data)):
            del data[i]['account']
            data[i]['created'] = gmt_conversor.convert_utctolocaltime(triggers[i].created)
            data[i]['modified'] = gmt_conversor.convert_utctolocaltime(triggers[i].modified)
            try:
                mail_list = MailList.objects.get(id=data[i]['mail_list'])
                mail_list = {
                    'id': mail_list.id,
                    'name': mail_list.name
                }
                data[0]['mail_list'] = mail_list
            except Exception as e:
                print(e)
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_fleet_trigger(request,id):
    try:
        trigger = FleetTrigger.objects.get(id=id,account=request.user.profile.account)
        serializer = FleetTriggerSerializer(trigger,many=False)
        data = serializer.data
        del data['account']
        data['created'] = gmt_conversor.convert_utctolocaltime(trigger.created)
        data['modified'] = gmt_conversor.convert_utctolocaltime(trigger.modified)
        try:
            mail_list = MailList.objects.get(id=data['mail_list'])
            mail_list = {
                'id': mail_list.id,
                'name': mail_list.name
            }
            data['mail_list'] = mail_list
        except Exception as e:
            print(e)
        if trigger.alert_type == 1003:
            data['extension1003'] = {
                'speed': trigger.extension1003.speed
            }
        elif trigger.alert_type == 1004:
            data['extension1004'] = {
                'geofences': [ {'id':x.id,'name':x.name} for x in trigger.extension1004.geofences.all() ]
            }
        elif trigger.alert_type == 1005:
            data['extension1005'] = {
                'geofences': [ {'id':x.id,'name':x.name} for x in trigger.extension1005.geofences.all() ]
            }
        elif trigger.alert_type == 1006:
            data['extension1006'] = {
                'speed': trigger.extension1006.speed,
                'geofences': [ {'id':x.id,'name':x.name} for x in trigger.extension1006.geofences.all() ]
            }
        elif trigger.alert_type == 1007:
            data['extension1007'] = {
                'seconds': trigger.extension1007.seconds,
                'geofences': [ {'id':x.id,'name':x.name} for x in trigger.extension1007.geofences.all() ]
            }
        elif trigger.alert_type == 1008:
            data['extension1008'] = {
                'seconds': trigger.extension1008.seconds,
                'geofences': [ {'id':x.id,'name':x.name} for x in trigger.extension1008.geofences.all() ]
            }
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_generic_fleet_trigger(request):
    data = request.data
    try:
        data['account'] = request.user.profile.account.id
    except Exception as e:
        error = {
            'detail': 'Account does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    if 'alert_type' in data:
        if data['alert_type'] not in [1001,1002,1009,1010,1011]:
            error = {
                'detail': 'Alert type not allowed.'
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTriggerSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1003_fleet_trigger(request):
    data = request.data
    serializer = FleetTrigger1003Serializer(data=data)
    if serializer.is_valid():
        extension1003 = FleetTriggerExtension1003.objects.create(
            speed = data['speed'],
            account = request.user.profile.account,
        )
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1003,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1003 = extension1003,
            account = request.user.profile.account
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    try:
        fleet_trigger.extension1003.delete()
    except Exception as e:
        print(e)
    try:
        fleet_trigger.extension1006.delete()
    except Exception as e:
        print(e)
    try:
        fleet_trigger.extension1007.delete()
    except Exception as e:
        print(e)
    try:
        fleet_trigger.extension1008.delete()
    except Exception as e:
        print(e)
    fleet_trigger.delete()
    response = {
        'status': 'OK',
        'description': 'Fleet trigger was deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_generic_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateFleetTriggerSerializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = data['alert_type']
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)