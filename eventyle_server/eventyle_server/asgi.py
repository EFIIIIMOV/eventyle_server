import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddleware, SessionMiddleware, CookieMiddleware
from django.core.asgi import get_asgi_application

from chat_app import routs

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventyle_server.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": CookieMiddleware(
        URLRouter(
            routs.websocket_urlpatterns
        ),
    ),
})
