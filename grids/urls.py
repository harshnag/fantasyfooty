from django.conf.urls import url

from . import views

app_name = 'grids'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<player_id>[0-9]+)/$', views.player, name='player'),
]
