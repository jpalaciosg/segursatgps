from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Alert
from .serializers import AlertSerializer
from units.models import Device
from .forms import ReportForm

from datetime import datetime

from common.gmt_conversor import GMTConversor

gmt_conversor = GMTConversor() #conversor zona horaria

# Create your views here.
@login_required
def alerts_view(request):
    return render(request,'alerts/alerts.html')

def alert_history_view(request):
    if request.method == 'POST':
        data = request.POST
        units = Device.objects.filter(account=request.user.profile.account)
        initial_timestamp = None
        final_timestamp = None
        form = ReportForm(data)
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
                    timestamp__lte=final_timestamp
                ).order_by('id')
                for alert in alerts:
                    dt = datetime.utcfromtimestamp(alert.timestamp)
                    dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                    alert.datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                return render(request,'alerts/alert-history.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':unit,
                    'units':units,
                    'alerts':alerts,
                })
            else:
                alerts = Alert.objects.using('history_db_replica').filter(
                    unitid=unit.id,
                    timestamp__gte=initial_timestamp,
                    timestamp__lte=final_timestamp
                ).order_by('id')
                for alert in alerts:
                    dt = datetime.utcfromtimestamp(alert.timestamp)
                    dt = gmt_conversor.convert_utctolocaltime(dt) # convertir a zona horaria
                    alert.datetime = dt.strftime("%d/%m/%Y %H:%M:%S")
                return render(request,'alerts/alert-history.html',{
                    'initial_datetime':data['initial_datetime'],
                    'final_datetime':data['final_datetime'],
                    'selected_unit':unit,
                    'units':units,
                    'alerts':alerts,
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
def alert_search(request,alert_date,unit_name):
    try:
        initial_timestamp = None
        final_timestamp = None
        try:
            date_time_str = f'{alert_date} 00:00:00'
            date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            initial_timestamp = datetime.timestamp(date_time_obj)
            final_timestamp = initial_timestamp+86400
        except Exception as e:
            error = {
                'error':str(e)
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        if unit_name == 'all':
            alerts = Alert.objects.filter(
            account = request.user.profile.account,
            timestamp__gte=initial_timestamp,
            timestamp__lte=final_timestamp
        )
        else:
            alerts = Alert.objects.filter(
                account = request.user.profile.account,
                unit_name = unit_name,
                timestamp__gte=initial_timestamp,
                timestamp__lte=final_timestamp
            )
        serializer = AlertSerializer(alerts,many=True)
        data = serializer.data
        for item in data:
            dt = datetime.fromtimestamp(item['timestamp'])
            item['datetime'] = dt.strftime("%Y/%m/%d %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        except Alert.DoesNotExist:
            unit_name = None
        serializer = AlertSerializer(alert, many=False)
        data = serializer.data
        data['unit_name'] = unit_name
        dt = datetime.fromtimestamp(data['timestamp'])
        data['datetime'] = dt.strftime("%Y/%m/%d %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)