from rest_framework import serializers
from .models import Account,Profile,User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data, request):
        del validated_data['password_confirmation']
        user = User.objects.create(**validated_data)
        profile_data = {
            "account": request.user.profile.account,
            "user": user
        }
        profile = Profile.objects.create(**profile_data)
        return user
    class Meta:
        model = User
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('__all__')