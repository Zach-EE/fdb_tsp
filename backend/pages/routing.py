from django.urls import path

from .consumers import ChartConsumer

ws_urlpatterns = [
    path('ws/pages/', ChartConsumer.as_asgi()),
]
