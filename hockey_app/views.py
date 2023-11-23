from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import * 
from django.contrib.auth import login, authenticate, logout


def index(request):
   # Render index.html
   players_registered = Player.objects.all()
   print("Player's registered to Adult Hockey League ", players_registered)
   return render( request, 'hockey_app/index.html', {'players_registered':players_registered})

class PlayerListView(generic.ListView):
   model = Player
class PlayerDetailView(generic.DetailView):
   model = Player


def createPlayer(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player')  # Redirect to the player list page
    else:
        form = PlayerForm()  # Create an empty form for GET requests
    return render(request, 'hockey_app/player_form.html', {'form': form})


def deletePlayer(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player')
    return render(request, 'hockey_app/player_delete.html', {'player': player})


def updatePlayer(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player-detail', pk=player.id)
    else:
        form = PlayerForm(instance=player)
    context = {'form': form, 'player': player}
    return render(request, 'hockey_app/update_player.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Change 'home' to your desired home page
    else:
        form = LoginForm()

    template_path = 'login.html'
    try:
        return render(request, template_path, {'form': form})
    except TemplateDoesNotExist:
        print(f"Template does not exist: {template_path}")
        raise  # Reraise the exception for detailed error information



def user_logout(request):
    logout(request)
    return redirect('login')