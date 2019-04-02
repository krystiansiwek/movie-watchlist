import django_tables2 as tables
from .models import MovieData


class WatchlistTable(tables.Table):
    class Meta:
        model = MovieData
        fields = ['movie_title', 'movie_premiere_year', 'movie_score']
        attrs = {'class': 'table table-hover text-danger'}
        template_name = 'watchlist/table_template.html'

    delete_movie = tables.TemplateColumn(template_name='watchlist/movie_delete_button.html', orderable=False)
