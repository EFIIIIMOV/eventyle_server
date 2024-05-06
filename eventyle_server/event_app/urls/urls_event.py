from django.urls import path

from event_app.views import views_event

urlpatterns = [
    path('', views_event.getAllEvents),
    path('event_id/<str:event_id>/', views_event.getEventByID),
    path('create/', views_event.createEvent),
    path('add_user/', views_event.addUserToEvent),
]
