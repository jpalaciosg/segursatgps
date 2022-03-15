from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from triggers.serializers import FleetTriggerSerializer

from .models import FleetTrigger

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
    for trigger in triggers:
        try:
            trigger.created = gmt_conversor.convert_utctolocaltime(trigger.created)
            trigger.modified = gmt_conversor.convert_utctolocaltime(trigger.modified)
        except Exception as e:
            print(e)
    return render(request,'triggers/fleet-trigger.html',{
        'triggers':triggers,
    })

@login_required
def delete_fleet_trigger(request,id):
    try:
        trigger = FleetTrigger.objects.get(id=id,account=request.user.profile.account)
        trigger.delete()
        messages.success('El trigger fue eliminado')
        return redirect('triggers')
    except:
        return redirect('triggers')

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