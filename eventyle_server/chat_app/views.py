from rest_framework_simplejwt.authentication import JWTAuthentication
import base64
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserChats(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    user_chats = models.UserChat.objects.filter(user_id=user_id).values('chat_id')
    chats = models.Chat.objects.filter(chat_id__in=user_chats).using('mysql')
    serializer = serializers.ChatSerializer(chats, many=True)
    return Response({'chats': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createChat(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    chat = models.Chat.objects.using('mysql').create(**request.data)
    chatSerializer = serializers.ChatSerializer(chat, many=False)

    userChat = models.UserChat.objects.using('mysql').create(user_id=user_id,
                                                             chat_id=request.data['chat_id'])

    userChatSerializer = serializers.UserChatSerializer(userChat, many=False)
    return Response({'chat': chatSerializer.data, 'chatUser': userChatSerializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserToChat(request):
    chat_id = request.data.get('chat_id')
    user_ids = request.data.get('user_ids', [])
    for user_id in user_ids:
        models.UserChat.objects.using('mysql').create(user_id=user_id, chat_id=chat_id)
    return Response({'message': 'Users added to chat successfully'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getChatImageByID(request):
    try:
        image_id = request.GET.get('image_id', '')
        chatImage = models.ChatImage.objects.using('mongo_db').get(_id=image_id)
        serializer = serializers.ChatImageSerializer(chatImage, many=False)
        image_binary = base64.b64decode(serializer.data['image'])
        return HttpResponse(image_binary, content_type="image/jpeg")
    except ObjectDoesNotExist:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addChatImage(request):
    try:
        image_id = request.data.get('image_id')
        image_base64 = request.data.get('image')
        image_binary = base64.b64decode(image_base64)
        chat_image = models.ChatImage(_id=image_id, image=image_binary)
        chat_image.save(using='mongo_db')
        return HttpResponse("Image uploaded successfully", status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllChatMessages(request):
    chat_id = request.GET.get('chat_id', '')
    messages = models.Message.objects.filter(chat_id=chat_id).using('mysql')
    serializer = serializers.MessageSerializer(messages, many=True)
    return Response({'messages': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createMessage(request):
    message = models.Message.objects.using('mysql').create(**request.data)
    serializer = serializers.MessageSerializer(message, many=False)
    return Response(serializer.data)
