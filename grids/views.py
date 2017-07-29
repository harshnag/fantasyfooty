from django.shortcuts import (get_object_or_404, get_list_or_404,
                render, redirect)
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.views import generic, View
import ast

from .forms import CreateGameForm
from .models import Player, GameBoard, Position, GameState, Team

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
                        (player_id, player_list.name))

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
            kickoff_pos = Position.objects.create(row=rows/2, col=col/2, board=gb)
            gs = GameState.objects.create(board=gb, active_position=kickoff_pos)
            return redirect('grids:gameboard', gameboard_id=gb.pk)
    else:
        form = CreateGameForm()

    context = {
               'form': form
               }
    return render(request, 'grids/gamesetup.html', context)

class Game(View):
    def post(self, request):
        return render(request, 'grids/gameboard.html', context)
        
    def get(self, request, gameboard_id):
        player_list = Player.objects.all()
        gameboard = get_object_or_404(GameBoard, id=gameboard_id)
        gameboard_array = ast.literal_eval(gameboard.gameboard)
        positions = Position.objects.filter(board__pk=gameboard_id)
        gamestate = GameState.objects.get(board__pk=gameboard_id)
        teams = gamestate.teams.all()
        
        for pos in positions:
            gameboard_array[pos.row][pos.col] = pos
        rows = gameboard.rows
        cols = gameboard.cols
        context = {
            'player_list' : player_list,
            'gameboard' : gameboard,
            'gameboard_array' : gameboard_array,
            'rows' : rows,
            'cols' : cols,
            'positions' : positions,
            'gamestate' : gamestate,
            'teams' : teams,
            }
        return render(request, 'grids/gameboard.html', context)

