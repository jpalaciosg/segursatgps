from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from datetime import datetime

from .models import Alert
from .serializers import AlertSerializer
from units.models import Device

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@login_required
def alerts_view(request):
    # verificar privilegios
    if privilege.view_latest_alerts(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    if request.user.profile.account.name == '20102427891_Civa_Interprovincial':
        return render(request,'alerts/civa-alert.html',{
            'navbar':navbar,
        })
    elif request.user.profile.account.name == '20603017847':
        return render(request,'alerts/hng-inversiones.html',{
            'navbar':navbar,
        })
    return render(request,'alerts/alerts.html',{
        'navbar':navbar,
    })

def alert_history_view(request):
    # verificar privilegios
    if privilege.view_alert_history(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = Device.objects.filter(account=request.user.profile.account)
    disable_navbar = request.GET.get('disablenavbar',None)
    try:
        disable_navbar = bool(int(disable_navbar))
    except Exception as e:
        disable_navbar = False
    navbar = not disable_navbar
    return render(request,'alerts/alert-history.html',{
        'units':units,
        'navbar':navbar,
    })

@api_view(['GET'])
def get_alert_history(request,initial_datetime,final_datetime,unit_name,alert_type):
    # verificar privilegios
    if privilege.view_latest_alerts(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    units = Device.objects.filter(account=request.user.profile.account)
    initial_timestamp = None
    final_timestamp = None
    try:
        initial_datetime_str = f"{initial_datetime}:00"
        initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
        # --
        initial_timestamp = datetime.timestamp(initial_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    #
    try:
        final_datetime_str = f"{final_datetime}:00"
        final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
        # convertir a zona horaria
        final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
        # --
        final_timestamp = datetime.timestamp(final_datetime_obj)
    except Exception as e:
        error = {
            'error':str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

    if unit_name.upper() == 'ALL':
        alerts_qs = Alert.objects.using('history_db_replica').filter(
            accountid=request.user.profile.account.id,
            timestamp__gte=initial_timestamp,
            timestamp__lte=final_timestamp,
            alert_type=alert_type
        ).order_by('id')
        alert_serializer = AlertSerializer(alerts_qs,many=True)
        alerts = alert_serializer.data
        for alert in alerts:
            try:
                unit = units.get(id=alert['unitid'])
                alert['unit_name'] = unit.name
                alert['unit_description'] = unit.description
            except Exception as e:
                print(e)
                alert['unit_name'] = alert['reference']
                alert['unit_description'] = ''
            dt = datetime.utcfromtimestamp(alert['timestamp'])
            dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
            alert['datetime'] = dt.strftime("%d/%m/%Y %H:%M:%S")
            if alert['alert_priority'] == 'L':
                alert['alert_priority'] = 'BAJA'
            elif alert['alert_priority'] == 'M':
                alert['alert_priority'] = 'MEDIA'
            elif alert['alert_priority'] == 'H':
                alert['alert_priority'] = 'ALTA'
            elif alert['alert_priority'] == 'M':
                alert['alert_priority'] = 'MUY ALTA'

        summarization = []
        for unit in units:
            count = alerts_qs.filter(unitid=unit.id).count()
            if count > 0:
                summarization.append({
                    'unit_name':unit.name,
                    'unit_description':unit.description,
                    'initial_datetime':initial_datetime,
                    'final_datetime':final_datetime,
                    'count':count,
                })
        response = {
            'alerts':alerts,
            'summarization':summarization,
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        try:
            unit = Device.objects.get(
                name=unit_name,
                account=request.user.profile.account,
            )
        except Exception as e:
            error = {
            'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        #
        alerts_qs = Alert.objects.using('history_db_replica').filter(
            unitid=unit.id,
            timestamp__gte=initial_timestamp,
            timestamp__lte=final_timestamp,
            alert_type=alert_type
        ).order_by('id')
        alert_serializer = AlertSerializer(alerts_qs,many=True)
        alerts = alert_serializer.data
        for alert in alerts:
            alert['unit_name'] = unit.name
            alert['unit_description'] = unit.description
            dt = datetime.utcfromtimestamp(alert['timestamp'])
            dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
            alert['datetime'] = dt.strftime("%d/%m/%Y %H:%M:%S")
        
        summarization = []
        for unit in units:
            count = alerts_qs.filter(unitid=unit.id).count()
            if count > 0:
                summarization.append({
                    'unit_name':unit.name,
                    'unit_description':unit.description,
                    'initial_datetime':initial_datetime,
                    'final_datetime':final_datetime,
                    'count':count,
                })
        response = {
            'alerts':alerts,
            'summarization':summarization,
        }
        return Response(response,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_alert(request,id):
    # verificar privilegios
    if privilege.view_latest_alerts(request) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    try:
        try:
            alert = Alert.objects.get(id=id)
        except Alert.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            unit = Device.objects.get(id=alert.unitid)
            unit_name = unit.name
            unit_description = unit.description
        except Alert.DoesNotExist:
            unit_name = None
            unit_description = None
        serializer = AlertSerializer(alert, many=False)
        data = serializer.data
        data['unit_name'] = unit_name
        data['unit_description'] = unit_description
        dt = datetime.utcfromtimestamp(data['timestamp'])
        dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
        data['datetime'] = dt.strftime("%Y/%m/%d %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)