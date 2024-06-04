from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from auth_app.models import UserProfileInfo
from . import models


class ProfileInfoSerializer(ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = '__all__'


class ProfilePostSerializer(ModelSerializer):
    class Meta:
        model = models.ProfilePost
        fields = '__all__'


class ProfilePostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfilePostImage
        fields = ('_id', 'image')
