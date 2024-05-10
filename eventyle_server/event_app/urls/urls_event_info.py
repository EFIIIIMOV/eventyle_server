from django.urls import path

from event_app.views import views_event_info

urlpatterns = [
    path('all/', views_event_info.getAllEventsInfo),
    path('', views_event_info.getAllEventInfoByEventID),
    path('create/', views_event_info.createEventInfo),
]
