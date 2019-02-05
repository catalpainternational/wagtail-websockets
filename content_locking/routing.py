from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/content_editing/(?P<room_name>.*)/', consumers.PresenceConsumer)
]
