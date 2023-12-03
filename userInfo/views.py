from django.shortcuts import render, redirect, get_object_or_404
from .forms import FavoriteArtistsForm
from django.shortcuts import render
from .models import FavoriteArtists
from django.contrib.auth.decorators import login_required


@login_required
def list_artists(request):
    artists = FavoriteArtists.objects.filter(user=request.user)
    return render(request, 'list_artists.html', {'artists': artists})


@login_required
def add_artist(request):
    if request.method == 'POST':
        form = FavoriteArtistsForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.user = request.user
            artist.save()
            return redirect('list_artists')
    else:
        form = FavoriteArtistsForm()
    return render(request, 'add_artist.html', {'form': form})


@login_required
def update_artist(request, pk):
    artist = get_object_or_404(FavoriteArtists, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FavoriteArtistsForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('list_artists')
    else:
        form = FavoriteArtistsForm(instance=artist)
    return render(request, 'update_artist.html', {'form': form})


@login_required
def delete_artist(request, pk):
    artist = get_object_or_404(FavoriteArtists, pk=pk, user=request.user)
    if request.method == 'POST':
        artist.delete()
        return redirect('list_artists')
    return render(request, 'delete_artist.html', {'artist': artist})
