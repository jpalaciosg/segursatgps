from rest_framework import serializers
from users.models import Account

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=50)
    device_timeout = serializers.IntegerField

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.device_timeout = validated_data.get('device_timeout', instance.device_timeout)
        instance.save()
        return instance