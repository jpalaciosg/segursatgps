from rest_framework import serializers
from .models import Device,Group

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('__all__')

class UpdateDeviceSerializer(serializers.Serializer):
    unit_name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200,allow_blank=True)
    odometer = serializers.FloatField()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')


