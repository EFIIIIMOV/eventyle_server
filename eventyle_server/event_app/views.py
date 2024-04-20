from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

@api_view(['GET'])
def getRoutes(request):
    return Response({'endpoint': 'hello world!'})

@api_view(['GET'])
def getAllEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({'events': serializer.data})

