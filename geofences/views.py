from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Geofence
from .serializers import GeofenceSerializer

# Create your views here.
@login_required
def geofences_view(request):
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    return render(request,'geofences/geofences.html',{
        'geofences':geofences,
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
def get_geofence(request,name):
    try:
        geofence = Geofence.objects.get(name=name,account=request.user.profile.account)
        serializer = GeofenceSerializer(geofence,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)