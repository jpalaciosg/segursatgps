from django.urls import re_path

#import locations.consumers as locations_consumers
from segursatgps.consumers import GenericConsumer

websocket_urlpatterns = [
    re_path(r'ws/locations/(?P<room_name>\w+)/$', GenericConsumer.as_asgi()),
]