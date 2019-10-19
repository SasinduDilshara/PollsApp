from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active', 'is_superuser',
                  'date_joined', 'last_login']


class AppUserSerializer(serializers.ModelSerializer):
    auth = UserSerializer(read_only=True)

    class Meta:
        model = AppUser
        fields = ['auth', 'snippet','number']

class AppUserSimpleSerializer(serializers.ModelSerializer):
    auth = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AppUser
        fields = ['auth', 'snippet','number']
