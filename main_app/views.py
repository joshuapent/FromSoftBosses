from django.shortcuts import render, redirect
from .models import Game, Boss
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BossForm


games = [
    {'title': 'Dark Souls', 'description': 'The first of the souls series', 'boss_number': 13},
    {'title': 'Dark Souls II', 'description': 'The second installment of the souls series', 'boss_number': 32},
    {'title': 'Dark Souls III', 'description': 'The final installment of the souls series', 'boss_number': 19},
]

# Create your views here.

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

def add_boss(request, game_id):
    form = BossForm(request.POST)
    if form.is_valid():
        new_boss = form.save(commit=False)
        new_boss.game_id = game_id
        new_boss.save()
    return redirect('show', game_id=game_id)


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
    bosses = Boss.objects.all()
    boss_form = BossForm()

    return render(request, 'games/show.html', {
        'game' : game,
        'boss_form': boss_form,
        'bosses': bosses
    })


