from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#from .models import Geofence

# Create your views here.
@login_required
def alerts_view(request):
    #geofences = Geofence.objects.filter(account=request.user.profile.account)
    return render(request,'alerts/alerts.html')