from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
import base64
from . import serializers


@api_view(['POST'])
def createUser(request):
    requestData = request.data
    try:
        if not all(
                key in requestData for key in ['user_id', 'email', 'password', 'role', 'name', 'surname', 'aboutUser']):
            return Response({'error': 'Не все необходимые данные предоставлены'}, status=400)

        models.EventyleUser.objects.create_user(id=requestData.get('user_id'),
                                                email=requestData.get('email'),
                                                password=requestData.get('password'))

        userProfileInfo = models.UserProfileInfo(
            user_id=requestData.get('user_id'),
            role=requestData.get('role'),
            name=requestData.get('name'),
            surname=requestData.get('surname'),
            description=requestData.get('aboutUser')
        )
        userProfileInfo.save(using='mysql')

        if requestData.get('image') != '':
            image_binary = base64.b64decode(requestData.get('image'))
            userProfileImage = models.UserProfileImage(_id=requestData.get('user_id'),
                                                       image=image_binary)
            userProfileImage.save(using='mongo_db')

        return Response({'User create successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
