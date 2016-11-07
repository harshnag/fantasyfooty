from django.contrib import admin

from .models import Rating, Player, GameBoard, Position, User, GameState

admin.site.register(Rating)
admin.site.register(Player)
admin.site.register(GameBoard)
admin.site.register(Position)
admin.site.register(User)
admin.site.register(GameState)
