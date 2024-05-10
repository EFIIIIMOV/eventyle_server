from django.urls import path

from event_app.views import views_event

urlpatterns = [
    path('all/', views_event.getAllEvents, name='get_all_events'),
    path('', views_event.getUserEvents, name='get_user_events'),
    path('create/', views_event.createEvent, name='create_event'),
    path('add_user/', views_event.addUserToEvent, name='add_user_to_event'),
]
