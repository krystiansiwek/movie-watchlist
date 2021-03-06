from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('watchlists/', views.watchlists, name='watchlists'),
    path('watchlists/<watchlist>', views.watchlist_view, name='watchlist_view'),
    path('watchlists/movie/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
    path('watchlists/<int:watchlist_id>/delete/', views.delete_watchlist, name='delete_watchlist'),
]
