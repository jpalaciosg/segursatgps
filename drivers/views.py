from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from bootstrap_modal_forms.generic import BSModalCreateView

from .models import Driver
from .forms import DriverModelForm
from .serializers import DriverSerializer

# Create your views here.
@login_required
def drivers_view(request):
    drivers = Driver.objects.filter(account=request.user.profile.account)
    return render(request,'drivers/drivers.html',{
        'drivers':drivers,
    })

@api_view(['GET'])
def get_drivers(request):
    try:
        drivers = Driver.objects.filter(account=request.user.profile.account)
        serializer = DriverSerializer(drivers,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_driver(request,id):
    try:
        driver = Driver.objects.get(id=id,account=request.user.profile.account)
        serializer = DriverSerializer(driver, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

class DriverCreateView(BSModalCreateView):
    template_name = 'drivers/create-driver.html'
    form_class = DriverModelForm
    success_message = 'Success: Driver was created.'
    success_url = reverse_lazy('drivers')