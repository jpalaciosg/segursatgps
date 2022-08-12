from rest_framework import serializers
from .models import Device,Group
from users.models import Account

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('__all__')

class UpdateDeviceSerializer(serializers.Serializer):
    unit_name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200,allow_blank=True)
    odometer = serializers.FloatField()

class GroupSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        units = validated_data['units']
        del validated_data['units']
        group = Group.objects.create(**validated_data)
        for id in units:
            try:
                device = Device.objects.get(id=id,account=account)
                group.units.add(device)
            except:
                pass
        return group
    class Meta:
        model = Group
        fields = ('__all__')


