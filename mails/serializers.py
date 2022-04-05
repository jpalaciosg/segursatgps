from rest_framework import serializers
from .models import MailList
from users.models import Account

class MailListSerializer(serializers.ModelSerializer):
    def create(self,validated_data,request):
        validated_data['account'] = request.user.profile.account
        mail_list = MailList.objects.create(**validated_data)
        return mail_list
    class Meta:
        model = MailList
        fields = ('__all__')

class UpdateMailListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    mails = serializers.CharField()
