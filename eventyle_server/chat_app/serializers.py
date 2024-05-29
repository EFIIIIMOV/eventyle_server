from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Chat, ChatImage, UserChat


class ChatSerializer(ModelSerializer):
    chat_id = serializers.UUIDField()

    class Meta:
        model = Chat
        fields = '__all__'


class ChatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatImage
        fields = ('_id', 'image')


class UserChatSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    chat_id = serializers.UUIDField()

    class Meta:
        model = UserChat
        fields = '__all__'
