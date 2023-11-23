from django.urls import path
from . import views
from .views import register, user_login, user_logout

urlpatterns = [
    path('', views.index, name='index'),
    path('player/', views.PlayerListView.as_view(), name= 'player'),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name='player-detail'),
    path('player/create_player/', views.createPlayer, name='create_player'),
    path('player/<int:pk>/delete/', views.deletePlayer, name='delete-player'),
    path('player/<int:pk>/update/', views.updatePlayer, name='update-player'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

