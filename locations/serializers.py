from rest_framework import serializers
from .models import Location,SutranLocation

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

class InsertLocationSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    deviceid = serializers.CharField(max_length=20)
    timestamp = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    altitude = serializers.IntegerField()
    speed = serializers.IntegerField()
    angle = serializers.IntegerField()
    protocol = serializers.CharField()
    address = serializers.CharField(max_length=500,allow_blank=True)

class SutranLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SutranLocation
        fields = ('__all__')