from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.views import generic
import ast

from .forms import CreateGameForm
from .models import Player, GameBoard

def index(request):
    player_list = Player.objects.all()
    games = GameBoard.objects.all()
    context = {
        'player_list' : player_list,
        'games' : games,
        }
    return render(request, 'grids/index.html', context)

def player(request, player_id):
    player_list = get_object_or_404(Player, id=player_id)
    return HttpResponse("Looking up player id: <<%s>> : %s" %
                        (player_id, player_list.player_name))

def gameboard(request, gameboard_id):
    player_list = Player.objects.all()
    gameboard = get_object_or_404(GameBoard, id=gameboard_id)
    gameboard_array = ast.literal_eval(gameboard.gameboard)
    rows = gameboard.rows
    cols = gameboard.cols
    context = {
        'player_list' : player_list,
        'gameboard' : gameboard,
        'gameboard_array' : gameboard_array,
        'rows' : rows,
        'cols' : cols,
        }
    return render(request, 'grids/gameboard.html', context)

def gamesetup(request):
    if(request.method == 'POST'):
        form = CreateGameForm(request.POST)

        if form.is_valid():
            rows = form.cleaned_data['rows']
            cols = form.cleaned_data['cols']
            board = []
            for row in range(rows):
                board.append([])
                for col in range(cols):
                    board[row].append('0')
            
            gb = GameBoard.objects.create(gameboard=board, rows=rows, cols=cols)
            return redirect('grids:gameboard', gameboard_id=gb.pk)
    else:
        form = CreateGameForm()

    context = {
               'form': form
               }
    return render(request, 'grids/gamesetup.html', context)
