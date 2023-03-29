from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bosses/', views.bosses_index, name='index'),
    path('lore/', views.lore, name='lore'),
    path('bosses/<int:boss_id>/', views.bosses_show, name='show')
]