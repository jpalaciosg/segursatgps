from email.policy import default
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
    address = serializers.CharField(max_length=500,allow_blank=True)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')

class InsertSutranLocationSerializer(serializers.Serializer):
    unit_name = serializers.CharField(max_length=50)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    speed = serializers.IntegerField()
    angle = serializers.IntegerField()

class InsertSolgasLocationSerializer(serializers.Serializer):
    provider = serializers.CharField(max_length=100)
    uniqueid = serializers.CharField(max_length=20)
    license_plate = serializers.CharField(max_length=20)
    timestamp = serializers.IntegerField(default=0)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    altitude = serializers.IntegerField(default=0)
    speed = serializers.IntegerField()
    angle = serializers.IntegerField(default=0)
    address = serializers.CharField(default="")
    ignition = serializers.BooleanField(default=False)
    panic = serializers.BooleanField(default=False)