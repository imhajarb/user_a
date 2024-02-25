from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


User = get_user_model()
class UserProfileChangeSerializer(ModelSerializer):
    username = CharField(required=False, allow_blank=True, initial="current username")
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        print('instance of username',instance.username)
        return instance

