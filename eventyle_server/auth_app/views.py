from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
from . import models
import base64
from . import serializers


@api_view(['POST'])
def createUser(request):
    try:
        data = request.data
        required_keys = ['user_id', 'email', 'password', 'role', 'name', 'surname', 'aboutUser']
        if not all(key in data for key in required_keys):
            return Response({'error': 'Не все необходимые данные предоставлены'}, status=400)

        with transaction.atomic():
            userAuthInfo = models.EventyleUser.objects.create_user(
                id=data['user_id'],
                email=data['email'],
                password=data['password']
            )

            userProfileInfo = models.UserProfileInfo.objects.using('mysql').create(
                user_id=data['user_id'],
                role=data['role'],
                name=data['name'],
                surname=data['surname'],
                description=data['aboutUser'],
            )

            if data.get('image') != '':
                userImageInfo = models.UserProfileImage.objects.using('mongo_db').create(
                    _id=data['user_id'],
                    image=base64.b64decode(data['image']),
                )

        return Response({'User create successfully'}, status=200)
    except Exception as e:
        try:
            userAuthInfo.delete()
            userProfileInfo.delete()
            userImageInfo.delete()
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    return Response({'error': str(e)}, status=500)
