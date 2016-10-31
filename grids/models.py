import datetime

from django.db import models
from django.utils import timezone

class Rating(models.Model):
    defense = models.IntegerField(default=0)
    offense = models.IntegerField(default=0)
    def __str__(self):
        return 'Off: %s, Def: %s' % (self.offense, self.defense)

class Player(models.Model):
    player_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth date')    
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    def __str__(self):
        return self.player_name

    def was_born_yesterday(self):
        return self.birth_date >= timezone.now() - datetime.timedelta(days=1)
        
