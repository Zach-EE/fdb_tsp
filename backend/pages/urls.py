from django.urls import path

from .views import IndexPageView, HomePageView, wsTest

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('test', wsTest),
    path('home', HomePageView.as_view(), name='home'),
]
