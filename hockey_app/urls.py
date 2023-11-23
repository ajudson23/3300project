from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('player/', views.PlayerListView.as_view(), name= 'player'),
path('player/<int:pk>/', views.PlayerDetailView.as_view(), name='player-detail'),
path('player/create_player/', views.createPlayer, name='create_player'),
path('player/<int:pk>/delete/', views.deletePlayer, name='delete-player'),
path('player/<int:pk>/update/', views.updatePlayer, name='update-player'),
]