from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.Serializer):
    deviceid = serializers.CharField(max_length=20)
    timestamp = serializers.IntegerField(default=0)
    latitude = serializers.FloatField(default=0.0)
    longitude = serializers.FloatField(default=0.0)
    altitude = serializers.IntegerField(default=0)
    speed = serializers.IntegerField(default=-1)
    angle = serializers.IntegerField(default=-1)