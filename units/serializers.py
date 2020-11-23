from rest_framework import serializers
from .models import Device,Unit

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('__all__')

class UnitSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(required=True)
    class Meta:
        model = Unit
        fields = ('name','device')