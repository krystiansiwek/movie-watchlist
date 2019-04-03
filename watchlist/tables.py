import django_tables2 as tables
from .models import MovieData


class WatchlistTable(tables.Table):
    numeration = tables.TemplateColumn('{{ row_counter|add:1 }}', verbose_name='#', orderable=False)
    delete_movie = tables.TemplateColumn(template_name='watchlist/movie_delete_button.html', orderable=False,
                                         verbose_name='Delete?')

    class Meta:
        model = MovieData
        fields = ['numeration', 'movie_title', 'movie_premiere_year', 'movie_score', 'delete_movie']
        attrs = {'class': 'table table-hover text-danger'}
        template_name = 'watchlist/table_template.html'


