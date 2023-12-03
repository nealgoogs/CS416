from django.db import models
from django.contrib.auth.models import User

GENRE_CATEGORIES = [
    ('rock', 'Rock'),
    ('pop', 'Pop'),
    ('hiphop', 'Hip Hop'),
    ('jazz', 'Jazz'),
    ('classical', 'Classical'),
]


class FavoriteArtists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_artists')
    artist_name = models.CharField(max_length=100)
    song_choice = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CATEGORIES)

    def __str__(self):
        return f"{self.artist_name} - {self.song_choice} ({self.genre})"
