from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json

from .models import Geofence, GeofenceGroup
from .serializers import GeofenceSerializer,UpdateGeofenceSerializer
from .forms import GeofenceCreateForm

from common.gmt_conversor import GMTConversor
from common.privilege import Privilege

gmt_conversor = GMTConversor() #conversor zona horaria
privilege = Privilege()

# Create your views here.
@login_required
def geofences_view(request):
    # verificar privilegios
    if privilege.view_geofences(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>",status=403)
    # fin - verificar privilegios
    geofences = Geofence.objects.filter(account=request.user.profile.account)
    for geofence in geofences:
        try:
            geofence.created = gmt_conversor.convert_localtimetoutc(geofence.created)
            geofence.modified = gmt_conversor.convert_localtimetoutc(geofence.modified)
        except Exception as e:
            print(e)
    return render(request,'geofences/geofences.html',{
        'geofences':geofences,
    })

@login_required
def geofence_group_view(request):
    # verificar privilegios
    if privilege.view_geofences(request.user.profile) == False:
        return HttpResponse("<h1>Acceso restringido</h1>",status=403)
    # fin - verificar privilegios
    geofence_groups = GeofenceGroup.objects.filter(account=request.user.profile.account)
    for gg in geofence_groups:
        try:
            gg.created = gmt_conversor.convert_localtimetoutc(gg.created)
            gg.modified = gmt_conversor.convert_localtimetoutc(gg.modified)
        except Exception as e:
            print(e)
    return render(request,'geofences/geofence-group.html',{
        'geofence_groups':geofence_groups,
    })

@api_view(['GET'])
def get_geofences(request):
    try:
        geofences = Geofence.objects.filter(account=request.user.profile.account)
        serializer = GeofenceSerializer(geofences,many=True)
        data = serializer.data
        for item in data:
            item['geojson'] = json.loads(item['geojson'])
        return Response(data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'detail':str(e)}
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
        error = {'detail':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_geofence(request):
    data = request.data
    try:
        data['account'] = request.user.profile.account.id
    except Exception as e:
        error = {
            'detail': 'Account does not exist.'
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = GeofenceSerializer(data=data)
    if serializer.is_valid():
        try:
            geojson = json.loads(data['geojson'])
        except Exception as e:
            error = {'errors':{
                'geojson': e
            }}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        serializer.create(data,request)
        response = {
            'status':'OK'
        }
        return Response(response,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_geofence(request,id):
    data = request.data
    try:
        geofence = Geofence.objects.get(id=id)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    serializer = UpdateGeofenceSerializer(data=data)
    if serializer.is_valid():
        geofence.name = data['name']
        geofence.description = data['description']
        geofence.geojson = data['geojson']
        geofence.show_geofence_on_map = data['show_geofence_on_map']
        geofence.save()
        return Response(data,status=status.HTTP_200_OK)
    else:
        error = {'errors':serializer.errors}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_geofence(request,id):
    try:
        geofence = Geofence.objects.get(id=id,account=request.user.profile.account)
    except Exception as e:
        error = {
            'detail': str(e)
        }
        return Response(error,status=status.HTTP_400_BAD_REQUEST)
    geofence.delete()
    response = {
        'status': 'OK',
        'description': 'Geofence was deleted.',
    }
    return Response(response,status=status.HTTP_200_OK)
