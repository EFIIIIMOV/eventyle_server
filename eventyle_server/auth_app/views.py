from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models


@api_view(['POST'])
def createUser(request):
    user_id = request.data.get('id', None)
    email = request.data.get('email', None)
    password = request.data.get('password', None)

    if email and password:
        user = models.EventyleUser.objects.create_user(id=user_id, email=email, password=password)
        return Response({'message': 'Пользователь успешно создан'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Необходимо предоставить логин, почту и пароль'}, status=status.HTTP_400_BAD_REQUEST)
