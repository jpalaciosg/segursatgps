from rest_framework import serializers
from .models import Geofence

class GeofenceSerializer(serializers.ModelSerializer):
    def create(self,validated_data,request):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        geofence = Geofence.objects.create(**validated_data)
        return geofence
    class Meta:
        model = Geofence
        fields = ('__all__')