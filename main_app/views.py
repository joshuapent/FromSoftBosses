from django.shortcuts import render
from .models import Game

games = [
    {'title': 'Dark Souls', 'description': 'The first of the souls series', 'boss_number': 13},
    {'title': 'Dark Souls II', 'description': 'The second installment of the souls series', 'boss_number': 32},
    {'title': 'Dark Souls III', 'description': 'The final installment of the souls series', 'boss_number': 19},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lore(request):
    return render(request, 'lore.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {
        'games': games
    })

def games_show(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/show.html', {
        'game' : game
    })