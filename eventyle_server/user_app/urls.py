from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    path('all/', views.GetAllUser),
    path('profile/', views.getProfileInfo),
    path('profiles/', views.getUsersInfo),
    path('profile/image/', views.getUserImage),
]
