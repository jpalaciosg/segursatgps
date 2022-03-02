from rest_framework import serializers
from .models import Device,Group

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('__all__')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')