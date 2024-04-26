from django.urls import path

from event_app.views import views_event_info

urlpatterns = [
    path('', views_event_info.getAllEventsInfo),
    path('info_id/<str:info_id>/', views_event_info.getEventInfoByID),
    path('event_id/<str:event_id>/', views_event_info.getAllEventInfoByEventID),
    path('create/', views_event_info.createEventInfo),
]
