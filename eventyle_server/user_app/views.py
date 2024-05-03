from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from auth_app import models
from . import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfileInfo(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    profileInfo = models.UserProfileInfo.objects.using('mysql').get(user_id=user_id)
    serializer = serializers.ProfileInfoSerializer(profileInfo, many=False)
    return Response({'profileInfo': serializer.data})
