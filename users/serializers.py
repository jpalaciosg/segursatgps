from rest_framework import serializers
from .models import Account,Profile,User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data, request):
        del validated_data['password_confirmation']
        user = User.objects.create(**validated_data)
        profile_data = {
            "account": request.user.profile.account,
            "user": user
        }
        profile = Profile.objects.create(**profile_data)
        return user
    class Meta:
        model = User
        fields = ('__all__')

class UpdateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=150, allow_blank=True)
    is_active = serializers.BooleanField

class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    password_confirmation = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('__all__')

class UpdateProfileSerializer(serializers.Serializer):
    is_admin = serializers.BooleanField()
    view_detailed_report = serializers.BooleanField()
    view_speed_report = serializers.BooleanField()
    view_stop_report = serializers.BooleanField()
    view_trip_report = serializers.BooleanField()
    view_day_trip_report = serializers.BooleanField()
    view_mileage_report = serializers.BooleanField()
    view_geofence_report = serializers.BooleanField()
    view_driving_style_report = serializers.BooleanField()
    view_telemetry_report = serializers.BooleanField()
    view_hours_report = serializers.BooleanField()
    view_temperature_report = serializers.BooleanField()
    view_detailed_report_with_attributes = serializers.BooleanField()
    view_group_trip_report = serializers.BooleanField()
    view_group_speed_report = serializers.BooleanField()
    view_group_mileage_report = serializers.BooleanField()
    view_group_stop_report = serializers.BooleanField()
    view_group_geofence_report = serializers.BooleanField()
    view_units = serializers.BooleanField()
    view_unit_triggers = serializers.BooleanField()
    view_fleet_triggers = serializers.BooleanField()
    view_mail_lists = serializers.BooleanField()
    view_geofences = serializers.BooleanField()
    view_users = serializers.BooleanField()
    view_latest_alerts = serializers.BooleanField()
    view_alert_history = serializers.BooleanField()
    units = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=20000)
    )