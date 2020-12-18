from django.urls import re_path

import locations.consumers as locations_consumers

websocket_urlpatterns = [
    re_path(r'ws/locations/(?P<room_name>\w+)/$', locations_consumers.LocationConsumer.as_asgi()),
]