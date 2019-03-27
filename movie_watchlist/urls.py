from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('watchlist.urls')),
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
