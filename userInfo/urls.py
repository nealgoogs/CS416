from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.list_artists, name='list_artists'),
    path('artists/add/', views.add_artist, name='add_artist'),
    path('artists/<int:pk>/edit/', views.update_artist, name='update_artist'),
    path('artists/<int:pk>/delete/', views.delete_artist, name='delete_artist'),
]