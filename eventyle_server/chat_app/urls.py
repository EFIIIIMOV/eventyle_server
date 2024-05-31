from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUserChats),
    path('create/', views.createChat),
    path('add_user/', views.addUserToChat),
    path('users/', views.getAllChatUsers),
    path('image/', views.getChatImageByID),
    path('add_image/', views.addChatImage),
    path('message/', views.getAllChatMessages),
    path('message/create/', views.createMessage),
]
