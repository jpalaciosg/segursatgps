from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import TriggerCreateForm
from .models import TriggerA

# Create your views here.
@login_required
def triggers_view(request):
    form = TriggerCreateForm()
    triggers = TriggerA.objects.filter(account=request.user.profile.account)
    return render(request,'alerts/triggers.html',{
        'triggers':triggers,
        'form':form,
    })