from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


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
