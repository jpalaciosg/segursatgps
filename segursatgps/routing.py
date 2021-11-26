from django.urls import re_path

import locations.consumers as locations_consumers
import alerts.consumers as alerts_consumers
import generic.consumers as generic_consumers

websocket_urlpatterns = [
    re_path(r'ws/locations/(?P<room_name>\w+)/$', locations_consumers.LocationConsumer.as_asgi()),
    re_path(r'ws/alert-listener/(?P<room_name>\w+)/$', alerts_consumers.AlertListenerConsumer.as_asgi()),
    re_path(r'ws/reload-listener/(?P<room_name>\w+)/$', generic_consumers.ReloadListenerConsumer.as_asgi()),
]