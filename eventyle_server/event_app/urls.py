from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllEvents),
    path('<int:id>/', views.getEventByID),
    path('create/', views.createEvent),
]
