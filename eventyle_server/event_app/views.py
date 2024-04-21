from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event


@api_view(['GET'])
def getAllEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({'events': serializer.data})


@api_view(['GET'])
def getEventByID(request, id):
    event = Event.objects.get(id=id)
    serializer = EventSerializer(event, many=False)
    return Response({'events': serializer.data})


@api_view(['POST'])
def createEvent(request):
    event = Event.objects.create(**request.data)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)
