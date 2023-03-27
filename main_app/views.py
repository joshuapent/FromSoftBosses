from django.shortcuts import render

bosses = [
    {'name': 'fume knight', 'game': 'Dark Souls 2', 'description': 'Powerful knight with dual swords'},
    {'name': 'Elden Beast', 'game': 'Elden Ring', 'description': 'Outer god of the lands between'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lore(request):
    return render(request, 'lore.html')

def bosses_index(request):
    return render(request, 'bosses/index.html', {
        'bosses': bosses
    })