import base64
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from event_app import models
from event_app import serializers


@api_view(['GET'])
def getAllEvents(request):
    events = models.Event.objects.all().order_by('date')
    serializer = serializers.EventSerializer(events, many=True)
    return Response({'events': serializer.data})


@api_view(['GET'])
def getEventByID(request, event_id):
    event = models.Event.objects.get(event_id=event_id)
    serializer = serializers.EventSerializer(event, many=False)
    return Response({'events': serializer.data})


@api_view(['POST'])
def createEvent(request):
    event = models.Event.objects.create(**request.data)
    serializer = serializers.EventSerializer(event, many=False)
    return Response(serializer.data)
