import base64
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from event_app import models
from event_app import serializers


@api_view(['GET'])
def getAllEventsInfo(request):
    eventsInfo = models.EventInfo.objects.all()
    serializer = serializers.EventInfoSerializer(eventsInfo, many=True)
    return Response({'eventInfo': serializer.data})


@api_view(['GET'])
def getEventInfoByID(request, info_id):
    eventInfo = models.EventInfo.objects.get(info_id=info_id)
    serializer = serializers.EventInfoSerializer(eventInfo, many=False)
    return Response({'event': serializer.data})


@api_view(['GET'])
def getAllEventInfoByEventID(request, event_id):
    eventsInfo = models.EventInfo.objects.filter(event_id=event_id)
    serializer = serializers.EventInfoSerializer(eventsInfo, many=True)
    return Response({'eventInfo': serializer.data})


@api_view(['POST'])
def createEventInfo(request):
    eventInfo = models.EventInfo.objects.create(**request.data)
    serializer = serializers.EventInfoSerializer(eventInfo, many=False)
    return Response(serializer.data)
