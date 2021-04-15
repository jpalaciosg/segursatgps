from rest_framework import serializers
from .models import Location

class InsertLocationSerializer(serializers.Serializer):
    deviceid = serializers.CharField(max_length=20)
    timestamp = serializers.IntegerField(default=0)
    latitude = serializers.FloatField(default=0.0)
    longitude = serializers.FloatField(default=0.0)
    altitude = serializers.IntegerField(default=0)
    speed = serializers.IntegerField(default=-1)
    angle = serializers.IntegerField(default=-1)
    protocol = serializers.CharField(max_length=100)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')