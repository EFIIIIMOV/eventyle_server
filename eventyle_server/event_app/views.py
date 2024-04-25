import base64

from django.http import HttpResponse
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


@api_view(['POST'])
def createEventInfo(request):
    eventInfo = models.EventInfo.objects.create(**request.data)
    serializer = serializers.EventInfoSerializer(eventInfo, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllEventImage(request):
    eventsImage = models.EventImage.objects.using('mongo_db').all()
    serializer = serializers.EventImageSerializer(eventsImage, many=True)
    return Response({'eventImage': serializer.data})


# @api_view(['GET'])
# def getEventImageByID(request, image_id):
#     eventsImage = models.EventImage.objects.using('mongo_db').get(_id=image_id)
#     serializer = serializers.EventImageSerializer(eventsImage, many=False)
#     return Response({'eventImage': serializer.data})

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
def getEventImageByID(request, image_id):
    try:
        eventsImage = models.EventImage.objects.using('mongo_db').get(_id=image_id)
        serializer = serializers.EventImageSerializer(eventsImage, many=False)
        image_binary = base64.b64decode(serializer.data['image'])
        return HttpResponse(image_binary, content_type="image/jpeg")
    except ObjectDoesNotExist:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)

