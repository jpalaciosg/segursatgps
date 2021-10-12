from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Alert
from .serializers import AlertSerializer
from units.models import Device
from .forms import AlertHistoryForm

from datetime import datetime

from common.gmt_conversor import GMTConversor

gmt_conversor = GMTConversor() #conversor zona horaria

# Create your views here.
@login_required
def alerts_view(request):
    return render(request,'alerts/alerts.html')

@login_required
def civa_alert_view(request):
    return render(request,'alerts/civa-alert.html')

def alert_history_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = AlertHistoryForm(data)
        if form.is_valid():
            unit = None
            if data['unit_name'].upper() != 'ALL':
                try:
                    unit = Device.objects.get(name=data['unit_name'])
                except Exception as e:
                    print(e)
                    form.add_error('unit_name', e)
            #
            try:
                initial_datetime_str = f"{data['initial_datetime']}:00"
                initial_datetime_obj = datetime.strptime(initial_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                initial_datetime_obj = gmt_conversor.convert_localtimetoutc(initial_datetime_obj)
                # --
                initial_timestamp = datetime.timestamp(initial_datetime_obj)
            except Exception as e:
                print(e)
                form.add_error('initial_date', e)
            #
            try:
                final_datetime_str = f"{data['final_datetime']}:00"
                final_datetime_obj = datetime.strptime(final_datetime_str, '%Y-%m-%d %H:%M:%S')
                # convertir a zona horaria
                final_datetime_obj = gmt_conversor.convert_localtimetoutc(final_datetime_obj)
                # --
                final_timestamp = datetime.timestamp(final_datetime_obj)
            except Exception as e:
                form.add_error('final_date', e)

            if len(form.errors) != 0:
                return render(request,'alerts/alert-history.html',{
                    'units':units,
                    'form':form,
                })

            if data['unit_name'].upper() == 'ALL':
                alerts = Alert.objects.using('history_db_replica').filter(
                    accountid=request.user.profile.account.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp,
                    alert_type=data['alert_type']
                ).order_by('id')
                for alert in alerts:
                    unit = units.get(id=alert.unitid)
                    alert.unit_name = unit.name
                    alert.unit_description = unit.description
                    dt = datetime.utcfromtimestamp(alert.timestamp)
                    dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                    alert.datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                summarization = []
                for unit in units:
                    count = alerts.filter(unitid=unit.id).count()
                    if count > 0:
                        summarization.append({
                            'unit_name':unit.name,
                            'unit_description':unit.description,
                            'count':count,
                        })
                return render(request,'alerts/alert-history.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':data['unit_name'],
                    'alert_type':data['alert_type'],
                    'units':units,
                    'alerts':alerts,
                    'summarization':summarization,
                })
            else:
                alerts = Alert.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp,
                    alert_type=data['alert_type']
                ).order_by('id')
                for alert in alerts:
                    alert.unit_name = unit.name
                    alert.unit_description = unit.description
                    dt = datetime.utcfromtimestamp(alert.timestamp)
                    dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                    alert.datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                summarization = []
                for unit in units:
                    count = alerts.filter(unitid=unit.id).count()
                    if count > 0:
                        summarization.append({
                            'unit_name':unit.name,
                            'unit_description':unit.description,
                            'count':count,
                        })
                return render(request,'alerts/alert-history.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':unit,
                    'alert_type':data['alert_type'],
                    'units':units,
                    'alerts':alerts,
                    'summarization':summarization,
                })
        return render(request,'alerts/alert-history.html',{
            'units':units,
            'form':form,
        })
    #GET
    units = Device.objects.filter(account=request.user.profile.account)
    return render(request,'alerts/alert-history.html',{
        'units':units,
    })

@api_view(['GET'])
def get_alert(request,id):
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