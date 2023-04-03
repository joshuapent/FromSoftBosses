from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_index, name='index'),
    path('lore/', views.lore, name='lore'),
    path('games/<int:game_id>/', views.games_show, name='show'),
    path('games/create', views.GameCreate.as_view(), name='create_game'),
    path('games/<int:pk>/remove/', views.GameDelete.as_view(), name='remove_game'),
    path('games/<int:pk>/edit/', views.GameUpdate.as_view(), name='edit_game'),
    path('games/<int:game_id>/add_boss/', views.add_boss, name='add_boss'),
    path('weaknesses/', views.WeaknessList.as_view(), name='weaknesses_index'),
    path('weaknesses/<int:pk>/', views.WeaknessDetail.as_view(), name='weakness_detail'),
    path('weaknesses/create/', views.WeaknessCreate.as_view(), name='weaknesses_create'),
    path('weaknesses/<int:pk>/update/', views.WeaknessUpdate.as_view(), name='weaknesses_update'),
    path('weaknesses/<int:pk>/delete/', views.WeaknessDelete.as_view(), name='weaknesses_delete'),
]