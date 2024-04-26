from django.urls import path

from event_app.views import views_event_image

urlpatterns = [
    path('', views_event_image.getAllEventImage),
    path('image_id/<str:image_id>', views_event_image.getEventImageByID),
    path('create/', views_event_image.addEventImage),
]
