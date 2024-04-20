from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Event


class EventSerializer(ModelSerializer):
    date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Event
        fields = '__all__'
