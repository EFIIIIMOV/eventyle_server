from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from event_app import swagger_docs
from event_app import models
from event_app import serializers


@swagger_docs.get_all_event_swagger_docs()
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllEvents(request):
    events = models.Event.objects.all().using('mysql').order_by('date')
    serializer = serializers.EventSerializer(events, many=True)
    return Response({'events': serializer.data})


@swagger_docs.get_user_event_swagger_docs()
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserEvents(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    user_events = models.UserEvent.objects.filter(user_id=user_id).values('event_id')
    events = models.Event.objects.filter(event_id__in=user_events).using('mysql').order_by('date')
    serializer = serializers.EventSerializer(events, many=True)
    return Response({'events': serializer.data})


@swagger_docs.post_new_event_swagger_docs()
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createEvent(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    event = models.Event.objects.using('mysql').create(**request.data)
    eventSerializer = serializers.EventSerializer(event, many=False)

    userEvent = models.UserEvent.objects.using('mysql').create(user_id=user_id,
                                                               event_id=request.data['event_id'])

    userEventSerializer = serializers.UserEventSerializer(userEvent, many=False)
    return Response({'event': eventSerializer.data, 'eventUser': userEventSerializer.data})


@swagger_docs.post_new_user_to_event_swagger_docs()
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserToEvent(request):
    event_id = request.data.get('event_id')
    user_ids = request.data.get('user_ids', [])
    for user_id in user_ids:
        models.UserEvent.objects.using('mysql').create(user_id=user_id, event_id=event_id)
    return Response({'message': 'Users added to event successfully'})
