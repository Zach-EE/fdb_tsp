from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # Local Apps
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]

