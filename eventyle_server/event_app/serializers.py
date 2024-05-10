from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Event, EventInfo, EventImage, UserEvent


class EventSerializer(ModelSerializer):
    date = serializers.DateField()
    event_id = serializers.UUIDField()

    class Meta:
        model = Event
        fields = '__all__'


class EventInfoSerializer(ModelSerializer):
    info_id = serializers.UUIDField()
    event_id = serializers.UUIDField()
    class Meta:
        model = EventInfo
        fields = '__all__'


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('_id', 'image')


class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = '__all__'
