from django.urls import path

from . import views

urlpatterns = [
    path('', views.getAllEvents),
    path('image/', views.getAllEventImage),
    path('image/image_id/<str:image_id>', views.getEventImageByID),
    path('event_id/<str:event_id>/', views.getEventByID),
    path('create/', views.createEvent),
    path('info/', views.getAllEventsInfo),
    path('info/info_id/<str:info_id>/', views.getEventInfoByID),
    path('info/event_id/<str:event_id>/', views.getAllEventInfoByEventID),
    path('info/create/', views.createEventInfo),
]
