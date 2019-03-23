from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('watchlist/<watchlist>', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/movie/<int:movie_id>', views.delete_movie, name='delete_movie')
]
