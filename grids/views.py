from django.shortcuts import render
from django.http import HttpResponse

from .models import Player

def index(request):
    player_list = Player.objects.all()
    output = ', '.join([p.player_name for p in player_list])
    return HttpResponse(output)

def player(request, player_id):
    return HttpResponse("You're not my buddy, friend <<%s>>." % player_id)
