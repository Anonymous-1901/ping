"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from ping.consumers import PersonalChatConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

application = get_asgi_application()
application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/',PersonalChatConsumer.as_asgi())
        ])
    )
})
