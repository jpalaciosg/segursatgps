from rest_framework import serializers
from users.models import Account,User,Profile
from units.models import Device

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')
 
class DeviceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        return Device.objects.create(**validated_data)
    class Meta:
        model = Device
        fields = ('__all__')
 
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data['account'])
        del validated_data['account']
        user = User.objects.create(**validated_data)
        profile_data = {
            "account": account,
            "user": user
        }
        profile = Profile.objects.create(**profile_data)
        return user
    class Meta:
        model = User
        fields = ('__all__')

class EditUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    is_admin = serializers.BooleanField()
    is_active = serializers.BooleanField()

class InsertLocationSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    deviceid = serializers.CharField(max_length=20)
    timestamp = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    altitude = serializers.IntegerField()
    speed = serializers.IntegerField()
    angle = serializers.IntegerField()
    protocol = serializers.CharField()
    address = serializers.CharField(max_length=400)

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(required=True)
    account = AccountSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('__all__')

class UpdateProfileSerializer(serializers.ModelSerializer):
    view_detailed_report = serializers.BooleanField()
    view_speed_report = serializers.BooleanField()
    view_stop_report = serializers.BooleanField()
    view_trip_report = serializers.BooleanField()
    view_mileage_report = serializers.BooleanField()
    view_geofence_report = serializers.BooleanField()
    view_driving_style_report = serializers.BooleanField()
    view_telemetry_report = serializers.BooleanField()
    view_detailed_report_with_attributes = serializers.BooleanField()
    view_group_trip_report = serializers.BooleanField()
    view_group_speed_report = serializers.BooleanField()
    view_group_mileage_report = serializers.BooleanField()
    view_group_stop_report = serializers.BooleanField()
    view_group_geofence_report = serializers.BooleanField()
    view_units = serializers.BooleanField()
    view_triggers = serializers.BooleanField()
    view_geofences = serializers.BooleanField()
    view_users = serializers.BooleanField()
    view_latest_alerts = serializers.BooleanField()
    view_alert_history = serializers.BooleanField()

class UpdatePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()