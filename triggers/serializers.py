from rest_framework import serializers

from .models import FleetTrigger,UnitTrigger
from mails.models import MailList
from users.models import Account
from units.models import Device

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

class FleetTrigger1012Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    seconds = serializers.IntegerField(min_value=60)

class UpdateFleetTriggerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    #alert_type = serializers.IntegerField()
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
        units = validated_data['units']
        del validated_data['units']
        unit_trigger = UnitTrigger.objects.create(**validated_data)
        for id in units:
            try:
                device = Device.objects.get(id=id,account=account)
                unit_trigger.units.add(device)
            except:
                pass
        unit_trigger.save()
        return unit_trigger
    class Meta:
        model = UnitTrigger
        fields = ('__all__')

class UnitTrigger1003Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    units = serializers.ListField(
        child=serializers.IntegerField()
    )
    speed = serializers.IntegerField()

class UnitTrigger1004and1005Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    units = serializers.ListField(
        child=serializers.IntegerField()
    )
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )

class UnitTrigger1006Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    units = serializers.ListField(
        child=serializers.IntegerField()
    )
    speed = serializers.IntegerField()
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )

class UnitTrigger1007and1008Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    alert_priority = serializers.ChoiceField(choices = PRIORITY_CHOICES)
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    units = serializers.ListField(
        child=serializers.IntegerField()
    )
    seconds = serializers.IntegerField(min_value=60)
    geofences = serializers.ListField(
        child=serializers.IntegerField()
    )

class UpdateUnitTriggerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    #alert_type = serializers.IntegerField()
    alert_priority = serializers.CharField()
    is_active = serializers.BooleanField()
    send_notification = serializers.BooleanField()
    send_mail_notification = serializers.BooleanField()
    mail_list = serializers.IntegerField(required=False)
    units = serializers.ListField(
        child=serializers.IntegerField()
    )