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

class UpdateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    is_active = serializers.BooleanField

class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    password_confirmation = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('__all__')