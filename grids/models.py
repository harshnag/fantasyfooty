import datetime
import numpy as np
import ast
import random

from django.db import models
from django.utils import timezone

class Rating(models.Model):
    defense = models.IntegerField(default=0)
    offense = models.IntegerField(default=0)

    def __str__(self):
        return 'Off: %s, Def: %s' % (self.offense, self.defense)

# The sports athletes represented in game
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
        return  "%s: %s " % (self.id, self.gameboard)
        

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
     
class Team(models.Model):
    name = models.CharField(max_length=200)
    player = models.ManyToManyField(Player)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.name, self.player.all())

class GameState(models.Model):
    home = 'home'
    away = 'away'
    TEAMS = (
        (home, 'Home Team'),
        (away, 'Away Team'),
    )

    homegoals = models.IntegerField(default=0)
    awaygoals = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    max_time = models.IntegerField(default=90)
    time_increment = models.IntegerField(default=5)
    current_turn = models.CharField(max_length=10, choices=TEAMS, default=home)
    board = models.ForeignKey(GameBoard, on_delete=models.CASCADE)
    active_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return "Gameboard id: %s Teams: %s" % (self.board.id, self.teams.all())

class Encounter:
    
    def combat(self, gamestate):
        homeplayer = gamestate.current_position.player(gamestate.teams.home)
        return self.combatb(boardposition.HomePlayer, boardposition.currentHomephase,
                            boardposition.AwayPlayer, boardposition.currentAwayphase)
    
    def combatb(self, home, currentHomephase, away, currentAwayphase):
        Homeroll = home[currentHomephase] * self.roll()
        Awayroll = away[currentAwayphase] * self.roll()
        if Homeroll > Awayroll:
            return 'home'
        elif Homeroll < Awayroll:
            return 'away'
        else:
            return 'no-one'
        
    def roll(self):
        return random.randint(1,10)
