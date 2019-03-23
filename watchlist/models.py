from django.db import models
from django.contrib.auth.models import User


class WatchList(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    watchlist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.watchlist_name


class MovieData(models.Model):
    watchlist_name = models.ForeignKey(WatchList,
                                       on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=250)
    movie_premiere_year = models.IntegerField('premiere year')
    movie_score = models.FloatField('score')

    def __str__(self):
        return self.movie_title
