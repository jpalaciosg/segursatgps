from rest_framework import serializers
from .models import Geofence

class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('__all__')