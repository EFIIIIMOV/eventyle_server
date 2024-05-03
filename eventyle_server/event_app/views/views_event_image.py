import base64
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from event_app import models
from event_app import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllEventImage(request):
    eventsImage = models.EventImage.objects.using('mongo_db').all()
    serializer = serializers.EventImageSerializer(eventsImage, many=True)
    return Response({'eventImage': serializer.data})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEventImage(request):
    try:
        image_id = request.data.get('image_id')
        image_base64 = request.data.get('image')
        image_binary = base64.b64decode(image_base64)
        event_image = models.EventImage(_id=image_id, image=image_binary)
        event_image.save(using='mongo_db')
        return HttpResponse("Image uploaded successfully", status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
