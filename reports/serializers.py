from rest_framework import serializers

class ReportSerializer(serializers.Serializer):
    unit_name = serializers.CharField(max_length=50)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()

class SpeedReportSerializer(serializers.Serializer):
    unit_name = serializers.CharField(max_length=50)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()
    speed_limit = serializers.IntegerField()

class GeofenceReportSerializer(serializers.Serializer):
    unit_name = serializers.CharField(max_length=50)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )