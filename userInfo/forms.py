from django import forms
from .models import FavoriteArtists

class FavoriteArtistsForm(forms.ModelForm):
    class Meta:
        model = FavoriteArtists
        fields = ['artist_name', 'song_choice', 'genre']