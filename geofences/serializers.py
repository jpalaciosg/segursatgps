from rest_framework import serializers
from .models import Geofence
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
    description = serializers.CharField()
    geojson = serializers.JSONField()
    show_geofence_on_map = serializers.BooleanField()
