from rest_framework import serializers
from .models import Geofence,GeofenceGroup
from users.models import Account

class GeofenceSerializer(serializers.ModelSerializer):
    def create(self,validated_data,request):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        geofence = Geofence.objects.create(**validated_data)
        return geofence
    class Meta:
        model = Geofence
        fields = ('__all__')

class UpdateGeofenceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True)
    geojson = serializers.JSONField()
    show_geofence_on_map = serializers.BooleanField()
    enable_speed = serializers.BooleanField()
    speed = serializers.IntegerField(min_value=0)

class GeofenceGroupSerializer(serializers.ModelSerializer):
    def create(self,validated_data,request):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        geofence_group = GeofenceGroup.objects.create(**validated_data)
        return geofence_group
    class Meta:
        model = GeofenceGroup
        fields = ('__all__')