from rest_framework import serializers
from users.models import Account
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
 