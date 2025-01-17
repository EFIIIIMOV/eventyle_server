from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Eventyle API",
        default_version='v1',
        description="Api for administration",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('events/', include('event_app.urls.urls_event')),
    path('events/image/', include('event_app.urls.urls_event_image')),
    path('events/info/', include('event_app.urls.urls_event_info')),
    path('user/', include('user_app.urls')),
    path('chats/', include('chat_app.urls')),
]

websocket_urlpatterns = [
    re_path('', include('chat_app.routs'))
]
