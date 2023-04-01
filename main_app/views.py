from django.shortcuts import render
from .models import Game

games = [
    {'title': 'Dark Souls', 'description': 'The first of the souls series', 'boss_number': 13},
    {'title': 'Dark Souls II', 'description': 'The second installment of the souls series', 'boss_number': 32},
    {'title': 'Dark Souls III', 'description': 'The final installment of the souls series', 'boss_number': 19},
    {'title': 'Bloodborne', 'description': 'A twist on the formula to a more gritty, offensive game', 'boss_number': 17},
    {'title': 'Sekiro', 'description': 'A complete 180 in fighting style and design, this game follows a shinobi in Japan', 'boss_number': 12},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lore(request):
    return render(request, 'lore.html')

def bosses_index(request):
    return render(request, 'bosses/index.html', {
        'games': games
    })

def bosses_show(request, boss_id):
    game = Game.objects.get(id=boss_id)
    return render(request, 'games/show.html', {
        'game' : game
    })