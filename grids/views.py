from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def player(request, player_id):
    return HttpResponse("You're not my buddy, friend <<%s>>." % player_id)
