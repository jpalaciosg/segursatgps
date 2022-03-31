from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from triggers.serializers import *
from .models import *
from mails.models import MailList
from geofences.models import Geofence

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.

# FLEET TRIGGER

@login_required
def fleet_trigger_view(request):
    # verificar privilegios
    if privilege.view_triggers(request.user.profile) == False:
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
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1003,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1003 = extension1003,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1004_fleet_trigger(request):
    data = request.data
    serializer = FleetTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        extension1004 = FleetTriggerExtension1004.objects.create(
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1004.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1004,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1004 = extension1004,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1005_fleet_trigger(request):
    data = request.data
    serializer = FleetTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        extension1005 = FleetTriggerExtension1005.objects.create(
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1005.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1005,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1005 = extension1005,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1006_fleet_trigger(request):
    data = request.data
    serializer = FleetTrigger1006Serializer(data=data)
    if serializer.is_valid():
        extension1006 = FleetTriggerExtension1006.objects.create(
            speed = data['speed'],
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1006.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1006,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1006 = extension1006,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1007_fleet_trigger(request):
    data = request.data
    serializer = FleetTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        extension1007 = FleetTriggerExtension1007.objects.create(
            seconds = data['seconds'],
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1007.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1007,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1007 = extension1007,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1008_fleet_trigger(request):
    data = request.data
    serializer = FleetTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        extension1008 = FleetTriggerExtension1008.objects.create(
            seconds = data['seconds'],
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1008.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        FleetTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1008,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1008 = extension1008,
            mail_list =  mail_list,
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
        #fleet_trigger.alert_type = data['alert_type']
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1003_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTrigger1003Serializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = 1003
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.extension1003.speed = data['speed']
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1004_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = 1004
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.extension1004.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                fleet_trigger.extension1004.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1005_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = 1005
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.extension1005.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                fleet_trigger.extension1005.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1006_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTrigger1006Serializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = 1006
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.extension1006.speed = data['speed']
        fleet_trigger.extension1006.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                fleet_trigger.extension1006.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1007_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = 1007
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.extension1007.seconds = data['seconds']
        fleet_trigger.extension1007.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                fleet_trigger.extension1007.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1008_fleet_trigger(request,id):
    data = request.data
    try:
        fleet_trigger = FleetTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = FleetTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        fleet_trigger.name = data['name']
        fleet_trigger.description = data['description']
        fleet_trigger.alert_type = 1008
        fleet_trigger.alert_priority = data['alert_priority']
        fleet_trigger.is_active = data['is_active']
        fleet_trigger.send_notification = data['send_notification']
        fleet_trigger.send_mail_notification = data['send_mail_notification']
        fleet_trigger.extension1008.seconds = data['seconds']
        fleet_trigger.extension1008.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                fleet_trigger.extension1008.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                fleet_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        fleet_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

# UNIT TRIGGER

@login_required
def unit_trigger_view(request):
    # verificar privilegios
    if privilege.view_triggers(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    triggers = UnitTrigger.objects.filter(account=request.user.profile.account)
    mail_lists = MailList.objects.filter(account=request.user.profile.account)
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    for trigger in triggers:
        try:
            trigger.created = gmt_conversor.convert_utctolocaltime(trigger.created)
            trigger.modified = gmt_conversor.convert_utctolocaltime(trigger.modified)
        except Exception as e:
            print(e)
    return render(request,'triggers/unit-trigger.html',{
        'triggers':triggers,
        'mail_lists':mail_lists,
        'geofences': geofences,
    })

@api_view(['GET'])
def get_unit_triggers(request):
    try:
        triggers = UnitTrigger.objects.filter(account=request.user.profile.account)
        serializer = UnitTriggerSerializer(triggers,many=True)
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
            data[i]['units'] = [ {'id':x.id,'name':x.name} for x in triggers[i].units.all() ]
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_unit_trigger(request,id):
    try:
        trigger = UnitTrigger.objects.get(id=id,account=request.user.profile.account)
        serializer = UnitTriggerSerializer(trigger,many=False)
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
        data['units'] = [ {'id':x.id,'name':x.name} for x in trigger.units.all() ]
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
def create_generic_unit_trigger(request):
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
    serializer = UnitTriggerSerializer(data=data)
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
def create_1003_unit_trigger(request):
    data = request.data
    serializer = UnitTrigger1003Serializer(data=data)
    if serializer.is_valid():
        extension1003 = UnitTriggerExtension1003.objects.create(
            speed = data['speed'],
            account = request.user.profile.account,
        )
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        unit_trigger = UnitTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1003,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1003 = extension1003,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1004_unit_trigger(request):
    data = request.data
    serializer = UnitTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        extension1004 = UnitTriggerExtension1004.objects.create(
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1004.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        unit_trigger = UnitTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1004,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1004 = extension1004,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1005_unit_trigger(request):
    data = request.data
    serializer = UnitTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        extension1005 = UnitTriggerExtension1005.objects.create(
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1005.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        unit_trigger = UnitTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1005,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1005 = extension1005,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1006_unit_trigger(request):
    data = request.data
    serializer = UnitTrigger1006Serializer(data=data)
    if serializer.is_valid():
        extension1006 = UnitTriggerExtension1006.objects.create(
            speed = data['speed'],
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1006.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        unit_trigger = UnitTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1006,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1006 = extension1006,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1007_unit_trigger(request):
    data = request.data
    serializer = UnitTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        extension1007 = UnitTriggerExtension1007.objects.create(
            seconds = data['seconds'],
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1007.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        unit_trigger = UnitTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1007,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1007 = extension1007,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_1008_unit_trigger(request):
    data = request.data
    serializer = UnitTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        extension1008 = UnitTriggerExtension1008.objects.create(
            seconds = data['seconds'],
            account = request.user.profile.account,
        )
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                extension1008.geofences.add(geofence)
            except Exception as e:
                print(e)
        mail_list = None
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(id=data['mail_list'])
            except Exception as e:
                print(e)
        unit_trigger = UnitTrigger.objects.create(
            name = data['name'],
            description = data['description'],
            alert_type = 1008,
            alert_priority = data['alert_priority'],
            is_active = data['is_active'],
            send_notification = data['send_notification'],
            send_mail_notification = data['send_mail_notification'],
            extension1008 = extension1008,
            mail_list =  mail_list,
            account = request.user.profile.account
        )
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_generic_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateUnitTriggerSerializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        #unit_trigger.alert_type = data['alert_type']
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1003_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UnitTrigger1003Serializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        unit_trigger.alert_type = 1003
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        unit_trigger.extension1003.speed = data['speed']
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1004_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UnitTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        unit_trigger.alert_type = 1004
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        unit_trigger.extension1004.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                unit_trigger.extension1004.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1005_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UnitTrigger1004and1005Serializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        unit_trigger.alert_type = 1005
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        unit_trigger.extension1005.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                unit_trigger.extension1005.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1006_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UnitTrigger1006Serializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        unit_trigger.alert_type = 1006
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        unit_trigger.extension1006.speed = data['speed']
        unit_trigger.extension1006.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                unit_trigger.extension1006.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        for id in data['units']:
            try:
                device = Device.objects.get(id=id,account=request.user.profile.account)
                unit_trigger.units.add(device)
            except:
                pass
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1007_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UnitTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        unit_trigger.alert_type = 1007
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        unit_trigger.extension1007.seconds = data['seconds']
        unit_trigger.extension1007.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                unit_trigger.extension1007.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_1008_unit_trigger(request,id):
    data = request.data
    try:
        unit_trigger = UnitTrigger.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UnitTrigger1007and1008Serializer(data=data)
    if serializer.is_valid():
        unit_trigger.name = data['name']
        unit_trigger.description = data['description']
        unit_trigger.alert_type = 1008
        unit_trigger.alert_priority = data['alert_priority']
        unit_trigger.is_active = data['is_active']
        unit_trigger.send_notification = data['send_notification']
        unit_trigger.send_mail_notification = data['send_mail_notification']
        unit_trigger.extension1008.seconds = data['seconds']
        unit_trigger.extension1008.geofences.clear()
        for item in data['geofences']:
            try:
                geofence = Geofence.objects.get(
                    id = item,
                    account = request.user.profile.account,
                )
                unit_trigger.extension1008.geofences.add(geofence)
            except Exception as e:
                print(e)
        if 'mail_list' in data:
            try:
                mail_list = MailList.objects.get(
                    id = data['mail_list'],
                    account = request.user.profile.account,
                )
                unit_trigger.mail_list = mail_list
            except Exception as e:
                print(e)
        unit_trigger.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)