from django.contrib import admin
from .models import MovieData, WatchList


class MovieDataInLine(admin.TabularInline):
    model = MovieData
    extra = 2


class WatchListsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author', {'fields': ['author']}),
        ('Watchlist name', {'fields': ['watchlist_name']})
    ]
    inlines = [MovieDataInLine]
    list_display = ('watchlist_name', 'author')


admin.site.register(WatchList, WatchListsAdmin)
