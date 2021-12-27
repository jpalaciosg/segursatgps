from rest_framework import serializers
from .models import Account,Profile,User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('__all__')