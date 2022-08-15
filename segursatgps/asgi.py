import os
import django

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'segursatgps.settings')
django.setup()

from channels.auth import AuthMiddlewareStack

import segursatgps.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            segursatgps.routing.websocket_urlpatterns
        )
    ),
})