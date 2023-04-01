from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.bosses_index, name='index'),
    path('lore/', views.lore, name='lore'),
    path('games/int:boss_id>/', views.bosses_show, name='show')
]