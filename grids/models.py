import datetime
import numpy as np
import ast

from django.db import models
from django.utils import timezone

class Rating(models.Model):
    defense = models.IntegerField(default=0)
    offense = models.IntegerField(default=0)

    def __str__(self):
        return 'Off: %s, Def: %s' % (self.offense, self.defense)

# The sports atheletes represented in game
class Player(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth date')    
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def was_born_yesterday(self):
        return self.birth_date >= timezone.now() - datetime.timedelta(days=1)

# The actual Human or AI player controlling the games
class User(models.Model):
    name = models.CharField(max_length=200)

class GameBoard(models.Model):
    default_board = "[['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]"
    gameboard = models.CharField(max_length=1024, default=default_board)
    rows = models.IntegerField(default=3)
    cols = models.IntegerField(default=4)
    
    def __str__(self):
        return self.gameboard
        
class Position(models.Model):
    row = models.IntegerField(default=0)
    col = models.IntegerField(default=0)
    board = models.ForeignKey(GameBoard, on_delete=models.CASCADE)
    player = models.ManyToManyField(Player)

    def __str__(self):
        players = []
        if self.player.all():
            for p in self.player.all():
                players.append(p.name)
        else:
            players = "none"

        pos = 'Row: %s Col: %s Player: %s' % (self.row, self.col, players)
        pos = pos + ' in %s' % self.board
        return pos
     

class GameState(models.Model):
    home = 'home'
    away = 'away'
    home_ai = 'home_ai'
    away_ai = 'away_ai'
    TEAMS = (
        (home, 'Home Team'),
        (away, 'Away Team'),
        (home_ai, 'Home Team (CPU)'),
        (away_ai, 'Away Team (CPU)'),
    )

    homegoals = models.IntegerField(default=0)
    awaygoals = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    max_time = models.IntegerField(default=90)
    time_increment = models.IntegerField(default=5)
    current_turn = models.CharField(max_length=10, choices=TEAMS, default=home)
    board = models.ForeignKey(GameBoard, on_delete=models.CASCADE)


