from watchlist.models import MovieData
import itertools


def get_fav_genres(request):
    user_genres = MovieData.objects.filter(watchlist_name__author=request.user).values_list('movie_genres', flat=True)
    user_genres = [user_genres[i].split(', ') for i in range(len(user_genres))]
    user_genres = list(itertools.chain(*user_genres))  # flattens list of lists to one list
    fav_genres = []
    for item in set(user_genres):
        if user_genres.count(item) > 5:
            fav_str = f'{item} - {user_genres.count(item)} movies'
            fav_genres.append(fav_str)

    return sorted(fav_genres, key=lambda x: -int(x.rsplit(' ', 2)[1]))  # return list sorted descending by number of movies
