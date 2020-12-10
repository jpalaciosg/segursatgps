from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Trigger,Alert
from .forms import TriggerCreateForm
from .serializers import AlertSerializer
from units.models import Unit
from datetime import datetime

# Create your views here.
@login_required
def alerts_view(request):
    account = request.user.profile.account
    alerts = Alert.objects.filter(account=account).order_by('-id')[:100]
    for alert in alerts:
        dt = datetime.fromtimestamp(alert.timestamp)
        alert.datetime = dt.strftime("%Y/%m/%d %H:%M:%S")
    return render(request,'alerts/alerts.html',{
        'alerts':alerts
    })

@login_required
def triggers_view(request):
    form = TriggerCreateForm()
    triggers = Trigger.objects.filter(account=request.user.profile.account)
    return render(request,'alerts/triggers.html',{
        'triggers':triggers,
        'form':form,
    })

@login_required
def alert_history_view(request):
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'alerts/alert-history.html',{
        'units':units
    })

@api_view(['GET'])
def alert_search(request,alert_date,unit_name):
    try:
        print(alert_date)
        if unit_name == 'all':
            alerts = Alert.objects.filter(
            account = request.user.profile.account
        )
        else:
            alerts = Alert.objects.filter(
                account = request.user.profile.account,
                unit_name = unit_name
            )
        serializer = AlertSerializer(alerts,many=True)
        data = serializer.data
        for item in data:
            dt = datetime.fromtimestamp(item['timestamp'])
            item['datetime'] = dt.strftime("%Y/%m/%d %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_alert(request,id):
    try:
        try:
            alert = Alert.objects.get(id=id)
        except Alert.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AlertSerializer(alert, many=False)
        data = serializer.data
        dt = datetime.fromtimestamp(data['timestamp'])
        data['datetime'] = dt.strftime("%Y/%m/%d %H:%M:%S")
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)