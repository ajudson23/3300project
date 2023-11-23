from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import * # <-- NEW


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