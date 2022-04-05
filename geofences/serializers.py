from rest_framework import serializers
from .models import Geofence

class GeofenceSerializer(serializers.ModelSerializer):
    def create(self,validated_data,request):
        validated_data['account'] = request.user.profile.account
        geofence = Geofence.objects.create(**validated_data)
        return geofence
    class Meta:
        model = Geofence
        fields = ('__all__')