from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from auth_app.models import UserProfileInfo


class ProfileInfoSerializer(ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = '__all__'
