from django.contrib import admin
from .models import FavoriteArtists


class FavoriteArtistsAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'song_choice', 'genre', 'user')
    search_fields = ('artist_name', 'genre', 'user__username')
    list_filter = ('genre', 'user')

admin.site.register(FavoriteArtists, FavoriteArtistsAdmin)
