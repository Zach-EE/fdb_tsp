from django.urls import path

from .views import IndexPageView, HomePageView, index

urlpatterns = [
    path('x', IndexPageView.as_view(), name='index'),
    path('', index),
    path('home', HomePageView.as_view(), name='home'),
]
