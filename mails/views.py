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
def mail_list_view(request):
    """
    # verificar privilegios
    if privilege.view_latest_alerts(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>", status=403)
    # fin - verificar privilegios
    mail_lists = FleetTrigger.objects.filter(account=request.user.profile.account)
    for mail_list in mail_lists:
        try:
            mail_list.created = gmt_conversor.convert_localtimetoutc(mail_list.created)
            mail_list.modified = gmt_conversor.convert_localtimetoutc(mail_list.modified)
        except Exception as e:
            print(e)
    """
    return render(request,'mails/mail-lists.html',{
    })