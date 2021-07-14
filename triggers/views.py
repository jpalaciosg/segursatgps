from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import TriggerCreateForm
from .models import FleetTrigger

# Create your views here.
@login_required
def fleet_trigger_view(request):
    form = TriggerCreateForm()
    triggers = FleetTrigger.objects.filter(account=request.user.profile.account)
    return render(request,'triggers/fleet-trigger.html',{
        'triggers':triggers,
        'form':form,
    })

@login_required
def delete_fleet_trigger(request,id):
    try:
        trigger = FleetTrigger.objects.get(id=id,account=request.user.profile.account)
        trigger.delete()
        return redirect('triggers')
    except:
        return redirect('triggers')