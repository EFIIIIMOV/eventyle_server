from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('events/', include('event_app.urls.urls_event')),
    path('events/image/', include('event_app.urls.urls_event_image')),
    path('events/info/', include('event_app.urls.urls_event_info')),
    path('user/', include('user_app.urls')),
]
