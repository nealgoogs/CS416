# Generated by Django 4.2.7 on 2023-11-28 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteArtists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100)),
                ('song_choice', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('hiphop', 'Hip Hop'), ('jazz', 'Jazz'), ('classical', 'Classical')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_artists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]