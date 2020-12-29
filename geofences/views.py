from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json

from .models import Geofence
from .serializers import GeofenceSerializer
from .forms import GeofenceCreateForm

# Create your views here.
@login_required
def geofences_view(request):
    form = GeofenceCreateForm
    if request.method == 'POST':
        form = GeofenceCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                geofence = Geofence.objects.get(
                    name = data['name'],
                    account = request.user.profile.account,
                )
            except Geofence.DoesNotExist:
                geofence = None
            if geofence:
                form.add_error('name', 'La geocerca ya existe.')
                form.add_error('geojson', 'La geocerca ya existe.')
            else:
                geofence = Geofence.objects.create(
                    name = data['name'],
                    description = data['description'],
                    geojson = data['geojson'],
                    account = request.user.profile.account
                )
                return redirect('geofences')
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    return render(request,'geofences/geofences.html',{
        'geofences':geofences,
        'form':form
    })

@api_view(['GET'])
def get_geofences(request):
    try:
        geofences = Geofence.objects.filter(account=request.user.profile.account)
        serializer = GeofenceSerializer(geofences,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_geofence(request,id):
    try:
        geofence = Geofence.objects.get(id=id,account=request.user.profile.account)
        serializer = GeofenceSerializer(geofence,many=False)
        data = serializer.data
        data['geojson'] = json.loads(data['geojson'])
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@login_required
def delete_geofence(request,id):
    try:
        geofence = Geofence.objects.get(id=id,account=request.user.profile.account)
        geofence.delete()
        return redirect('geofences')
    except:
        return redirect('geofences')