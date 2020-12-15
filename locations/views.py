from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Location
from .serializers import LocationSerializer

# Create your views here.
@api_view(['POST'])
def insert_location(request):
    data = request.data
    serializer = LocationSerializer(data=data)
    if serializer.is_valid():
        alert = serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)