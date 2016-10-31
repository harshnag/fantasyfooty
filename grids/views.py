from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Player

def index(request):
    player_list = Player.objects.all()
    context = {
        'player_list' : player_list
        }
    return render(request, 'grids/index.html', context)

def player(request, player_id):
    player_list = get_object_or_404(Player, id=player_id)
    return HttpResponse("Looking up player id: <<%s>> : %s" %
                        (player_id, player_list.player_name))
