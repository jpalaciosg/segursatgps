from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import TriggerCreateForm
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
    form = TriggerCreateForm()
    triggers = FleetTrigger.objects.filter(account=request.user.profile.account)
    for trigger in triggers:
        try:
            trigger.created = gmt_conversor.convert_localtimetoutc(trigger.created)
            trigger.modified = gmt_conversor.convert_localtimetoutc(trigger.modified)
        except Exception as e:
            print(e)
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