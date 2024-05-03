import base64
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from event_app import models
from event_app import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllEventsInfo(request):
    eventsInfo = models.EventInfo.objects.using('mysql').all()
    serializer = serializers.EventInfoSerializer(eventsInfo, many=True)
    return Response({'eventInfo': serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEventInfoByID(request, info_id):
    eventInfo = models.EventInfo.objects.using('mysql').get(info_id=info_id)
    serializer = serializers.EventInfoSerializer(eventInfo, many=False)
    return Response({'event': serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllEventInfoByEventID(request, event_id):
    user_id = JWTAuthentication().authenticate(request)[0].id
    if not models.UserEvent.objects.using('mysql').filter(event_id=event_id, user_id=user_id).exists():
        return Response({'error': 'Пользователь не имеет доступа к этому событию'}, status=status.HTTP_403_FORBIDDEN)
    eventsInfo = models.EventInfo.objects.using('mysql').filter(event_id=event_id)
    serializer = serializers.EventInfoSerializer(eventsInfo, many=True)
    return Response({'eventInfo': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createEventInfo(request):
    eventInfo = models.EventInfo.objects.using('mysql').create(**request.data)
    serializer = serializers.EventInfoSerializer(eventInfo, many=False)
    return Response(serializer.data)
