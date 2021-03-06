from django.conf.urls import url

from . import views
from .views import Game

app_name = 'grids'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<player_id>[0-9]+)/$', views.player, name='player'),
    url(r'^gameboard/(?P<gameboard_id>[0-9]+)/$', Game.as_view(), name='gameboard'),
    url(r'^gamesetup/$', views.gamesetup, name='gamesetup'),
]
