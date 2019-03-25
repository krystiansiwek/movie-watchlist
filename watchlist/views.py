import requests

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import MovieData, WatchList
from movie_watchlist.secret_settings import api_key


@login_required
def homepage(request):
    user_watchlists = WatchList.objects.filter(author=request.user)
    context = {
        'user_watchlists': user_watchlists,
    }
    if request.method == 'POST':
        new_watchlist_name = request.POST.get('new_watchlist_name')

        if WatchList.objects.filter(watchlist_name=new_watchlist_name, author=request.user).exists():
            messages.error(request, 'Watchlist with given name already exists.')
            return render(request,
                          'watchlist/homepage.html',
                          context)

        else:
            new_watchlist = WatchList(author=request.user, watchlist_name=new_watchlist_name)
            new_watchlist.save()
            return redirect('watchlist:add_to_watchlist', watchlist=new_watchlist_name)

    return render(request,
                  'watchlist/homepage.html',
                  context)


@login_required
def add_to_watchlist(request, watchlist):
    current_watchlist = get_object_or_404(WatchList, watchlist_name=watchlist, author=request.user)
    movies_in_watchlist = MovieData.objects.filter(watchlist_name=current_watchlist).order_by('pk')
    context = {
        'movies': movies_in_watchlist,
    }
    if request.method == 'POST':
        searched_title = request.POST.get('movie_title')
        api_url = f'http://www.omdbapi.com/?apikey={api_key}&t={searched_title}'
        api_request = requests.get(api_url)

        json_data = api_request.json()

        if json_data.get('Error'):
            messages.error(request, 'Movie not found.')
            return render(request,
                          'watchlist/add_to_watchlist.html',
                          context)
        else:
            title = json_data['Title']
            score = float(json_data['imdbRating'])
            premiere_year = int(json_data['Year'][:4])

            added_movie = MovieData(watchlist_name=current_watchlist,
                                    movie_title=title,
                                    movie_premiere_year=premiere_year,
                                    movie_score=score)
            added_movie.save()

        return render(request,
                      'watchlist/add_to_watchlist.html',
                      context)

    return render(request,
                  'watchlist/add_to_watchlist.html',
                  context)


@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(MovieData, pk=movie_id)

    if request.method == 'POST':
        movie.delete()
    return redirect('watchlist:add_to_watchlist', watchlist=movie.watchlist_name)


@login_required
def delete_watchlist(request, watchlist_id):
    watchlist = get_object_or_404(WatchList, pk=watchlist_id)

    if request.method == 'POST':
        watchlist.delete()
    return redirect('watchlist:homepage')
