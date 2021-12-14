from rest_framework import serializers

class DrivingStyleSerializer(serializers.Serializer):
    timestamp = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    altitude = serializers.IntegerField()
    speed = serializers.IntegerField()
    angle = serializers.IntegerField()
    ignition = serializers.BooleanField()
    driving = serializers.CharField()
    intensity = serializers.CharField()
    address = serializers.CharField()