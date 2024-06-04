from rest_framework_simplejwt.authentication import JWTAuthentication
import base64
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from . import swagger_docs
from auth_app import serializers as auth_serializers
from auth_app import models as auth_models
from . import models
from . import serializers


@swagger_docs.get_all_users_swagger_docs()
@api_view(['GET'])
def GetAllUser(requests):
    users = auth_models.UserProfileInfo.objects.using('mysql').all()
    serializer = auth_serializers.UserProfileInfoSerializer(users, many=True)
    return Response({'users': serializer.data})


@swagger_docs.get_searching_user_profile_swagger_docs()
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsersInfo(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    searchQuery = request.GET.get('searchQuery', '')
    users = auth_models.UserProfileInfo.objects.using('mysql').exclude(user_id=user_id).filter(
        Q(name__icontains=searchQuery) | Q(surname__icontains=searchQuery) | Q(role__icontains=searchQuery)
    )
    return Response({'users': auth_serializers.UserProfileInfoSerializer(users, many=True).data})


@swagger_docs.get_user_profile_info_swagger_docs()
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfileInfo(request):
    user_id = JWTAuthentication().authenticate(request)[0].id
    profileInfo = auth_models.UserProfileInfo.objects.using('mysql').get(user_id=user_id)
    serializer = auth_serializers.UserProfileInfoSerializer(profileInfo, many=False)
    return Response({'profileInfo': serializer.data})


@swagger_docs.get_user_profile_image_swagger_docs()
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getUserImage(request):
    try:
        user_id = request.GET.get('user_id', '')
        eventsImage = auth_models.UserProfileImage.objects.using('mongo_db').get(_id=user_id)
        serializer = auth_serializers.UserProfileImageSerializer(eventsImage, many=False)
        image_binary = base64.b64decode(serializer.data['image'])
        return HttpResponse(image_binary, content_type="image/jpeg")
    except ObjectDoesNotExist:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPost(request):
    requestData = request.data
    user_id = JWTAuthentication().authenticate(request)[0].id
    post = models.ProfilePost.objects.using('mysql').create(
        post_id=requestData['post_id'],
        user_id=user_id,
        post_text=requestData['postText'],
    )
    imageIds = requestData.get('imageIds', [])

    for imageId in imageIds:
        models.PostImage.objects.using('mysql').create(post_id=requestData['post_id'], image_id=imageId)

    profilePostSerializer = serializers.ProfilePostSerializer(post, many=False)
    return Response({'post': profilePostSerializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addPostImage(request):
    images = request.data
    for image in images:
        post_image = models.ProfilePostImage(_id=image['image_id'],
                                             image=base64.b64decode(image['image']))
        post_image.save(using='mongo_db')

    return HttpResponse("Image uploaded successfully", status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllPostByUserID(request):
    user_id = request.GET.get('user_id', '')
    posts = models.ProfilePost.objects.using('mysql').filter(user_id=user_id)
    serializerPost = serializers.ProfilePostSerializer(posts, many=True)
    posts = []
    for post in serializerPost.data:
        postImages = models.PostImage.objects.using('mysql').filter(post_id=post['post_id'])
        image_ids = [image.image_id for image in postImages]
        posts.append(models.ProfilePostImageForClient(post_id=post['post_id'],
                                                      user_id=post['user_id'],
                                                      post_text=post['post_text'],
                                                      images=image_ids))

    serializer = serializers.ProfilePostImageForClientSerializer(posts, many=True)
    return Response({'posts': serializer.data})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getEventImageByID(request):
    try:
        image_id = request.GET.get('image_id', '')
        postImage = models.ProfilePostImage.objects.using('mongo_db').get(_id=image_id)
        serializer = serializers.ProfilePostImageSerializer(postImage, many=False)
        image_binary = base64.b64decode(serializer.data['image'])
        return HttpResponse(image_binary, content_type="image/jpeg")
    except ObjectDoesNotExist:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)
