from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Unit
from .serializers import UnitSerializer

# Create your views here.  
@login_required
def units_view(request):
    units = Unit.objects.filter(account=request.user.profile.account)
    return render(request,'units/units.html',{
        'units':units,
    })

@api_view(['GET'])
def get_units(request):
    try:
        units = Unit.objects.filter(account=request.user.profile.account)
        return Response(units,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_unit(request,name):
    try:
        unit = Unit.objects.get(name=name,account=request.user.profile.account)
        serializer = UnitSerializer(unit,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        error = {'error':str(e)}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)