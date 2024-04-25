from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Event, EventInfo, EventImage


class EventSerializer(ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = Event
        fields = '__all__'


class EventInfoSerializer(ModelSerializer):
    class Meta:
        model = EventInfo
        fields = '__all__'


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('_id', 'image')
