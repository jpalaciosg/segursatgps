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

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')