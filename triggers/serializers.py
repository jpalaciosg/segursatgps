from rest_framework import serializers
from .models import FleetTrigger
from users.models import Account

class FleetTriggerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        mail_list = FleetTrigger.objects.create(**validated_data)
        return mail_list
    class Meta:
        model = FleetTrigger
        fields = ('__all__')

class UpdateFleetTriggerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_type = serializers.IntegerField()
    alert_priority = serializers.CharField()
    is_active = serializers.BooleanField()
