from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.GetAllUser),
    path('profile/', views.getProfileInfo),
    path('profiles/', views.getUsersInfo),
    path('profile/image/', views.getUserImage),
    path('profile/post/create/', views.createPost),
    path('profile/post/add_image/', views.addPostImage),
]
