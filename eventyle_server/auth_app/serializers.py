from rest_framework.serializers import ModelSerializer

from .models import UserProfileInfo, UserProfileImage


class UserProfileInfoSerializer(ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = '__all__'


class UserProfileImageSerializer(ModelSerializer):
    class Meta:
        model = UserProfileImage
        fields = '__all__'
