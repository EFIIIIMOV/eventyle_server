from rest_framework_simplejwt.authentication import JWTAuthentication
import base64
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from auth_app import serializers
from auth_app import models
#from . import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsersInfo(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    searchQuery = request.GET.get('searchQuery', '')
    users = models.UserProfileInfo.objects.using('mysql').exclude(user_id=user_id).filter(
        Q(name__icontains=searchQuery) | Q(surname__icontains=searchQuery) | Q(role__icontains=searchQuery)
    )
    return Response({'users': serializers.UserProfileInfoSerializer(users, many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfileInfo(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    profileInfo = models.UserProfileInfo.objects.using('mysql').get(user_id=user_id)
    serializer = serializers.UserProfileInfoSerializer(profileInfo, many=False)
    return Response({'profileInfo': serializer.data})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getUserImage(request):
    try:
        user_id = request.GET.get('user_id', '')
        eventsImage = models.UserProfileImage.objects.using('mongo_db').get(_id=user_id)
        serializer = serializers.UserProfileImageSerializer(eventsImage, many=False)
        image_binary = base64.b64decode(serializer.data['image'])
        return HttpResponse(image_binary, content_type="image/jpeg")
    except ObjectDoesNotExist:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)
