from django.shortcuts import render, redirect
from .models import Game, Boss, Weakness
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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

class WeaknessList(ListView):
    model = Weakness

class WeaknessDetail(DetailView):
    model = Weakness

class WeaknessCreate(CreateView):
  model = Weakness
  fields = '__all__'

class WeaknessUpdate(UpdateView):
  model = Weakness
  fields = ['name']

class WeaknessDelete(DeleteView):
  model = Weakness
  success_url = '/weaknesses'

def assign_weakness(request, game_id, weakness_id):
    Game.objects.get(id=game_id).weaknesses.add(weakness_id)
    return redirect('show', game_id=game_id)

def unassign_weakness(request, game_id, weakness_id):
    Game.objects.get(id=game_id).weaknesses.remove(weakness_id)
    return redirect('show', game_id=game_id)

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
    id_list = Game.weaknesses.all().values_list('id')
    weaknesses_game_doesnt_have = Game.objects.exclude(id__in=id_list)
    boss_form = BossForm()

    return render(request, 'games/show.html', {
        'game' : game,
        'boss_form': boss_form,
        'bosses': bosses,
        'weaknesses': weaknesses_game_doesnt_have
    })


