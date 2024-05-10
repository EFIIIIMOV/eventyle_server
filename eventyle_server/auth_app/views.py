from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
from . import models
import base64
from . import serializers


@swagger_auto_schema(
    methods=['post'],
    operation_summary="Регистрирует нового пользователя",
    operation_description="Данный эндпоинт создает новую запись о пользователе в auth_DB info_DB image_DB",
    responses={200: "OK"},
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            'role': openapi.Schema(type=openapi.TYPE_STRING),
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'surname': openapi.Schema(type=openapi.TYPE_STRING),
            'aboutUser': openapi.Schema(type=openapi.TYPE_STRING),
        }
    )
)
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
