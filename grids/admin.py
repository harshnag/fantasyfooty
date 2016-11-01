from django.contrib import admin

from .models import Rating, Player, GameBoard

admin.site.register(Rating)
admin.site.register(Player)
admin.site.register(GameBoard)
