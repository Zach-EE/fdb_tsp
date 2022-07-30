from django.urls import path

from .views import IndexPageView, HomePageView

urlpatterns = [
    path('index', IndexPageView.as_view(), name='index'),
    path('', HomePageView.as_view(), name='home'),
]
