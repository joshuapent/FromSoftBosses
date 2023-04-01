from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='index'),
    path('lore/', views.lore, name='lore'),
    path('games/<int:game_id>/', views.games_show, name='show')
]