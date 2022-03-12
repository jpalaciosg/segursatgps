from rest_framework import serializers
from .models import MailList

class MailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailList
        fields = ('__all__')


