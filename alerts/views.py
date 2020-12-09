from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Trigger,Alert
from .forms import TriggerCreateForm
from units.models import Unit

# Create your views here.
@login_required
def alerts_view(request):
    account = request.user.profile.account
    alerts = Alert.objects.filter(account=account).order_by('-id')[:100]
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