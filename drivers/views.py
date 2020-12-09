from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Driver
from .forms import DriverCreateForm
from .serializers import DriverSerializer

# Create your views here.

@login_required
def drivers_view(request):
    form = DriverCreateForm()
    if request.method == 'POST':
        form = DriverCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                driver = Driver.objects.get(id=data['id'])
            except Driver.DoesNotExist:
                driver = None
            if driver:
                form.add_error('id', 'El numero de documento ya existe.')
            else:
                driver = Driver.objects.create(
                    id = data['id'],
                    firstname = data['firstname'],
                    lastname = data['lastname'],
                    account = request.user.profile.account
                )
                return redirect('drivers')
    drivers = Driver.objects.filter(account=request.user.profile.account)
    return render(request,'drivers/drivers.html',{
        'drivers':drivers,
        'form':form,
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