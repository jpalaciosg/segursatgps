from rest_framework import serializers

from mails.models import MailList
from .models import FleetTrigger,UnitTrigger
from users.models import Account

PRIORITY_CHOICES = [
    ('L', 'LOW'),
    ('M', 'MEDIUM'),
    ('H', 'HIGH'),
    ('V', 'VERY HIGH'),
]

# FLEET TRIGGER SERIALIZERS

class FleetTriggerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        try:
            mail_list = MailList.objects.get(id=validated_data['mail_list'])
            validated_data['mail_list'] = mail_list
        except:
            pass
        fleet_trigger = FleetTrigger.objects.create(**validated_data)
        return fleet_trigger
    class Meta:
        model = FleetTrigger
        fields = ('__all__')

class FleetTrigger1003Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    speed = serializers.IntegerField()

class FleetTrigger1004and1005Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )

class FleetTrigger1006Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    speed = serializers.IntegerField()
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )

class FleetTrigger1007and1008Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    seconds = serializers.IntegerField(min_value=60)
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )

class UpdateFleetTriggerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_type = serializers.IntegerField()
    alert_priority = serializers.CharField()
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)


# UNIT TRIGGER SERIALIZERS

class UnitTriggerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data['account'])
        validated_data['account'] = account
        try:
            mail_list = MailList.objects.get(id=validated_data['mail_list'])
            validated_data['mail_list'] = mail_list
        except:
            pass
        unit_trigger = UnitTrigger.objects.create(**validated_data)
        return unit_trigger
    class Meta:
        model = UnitTrigger
        fields = ('__all__')