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
    path('games/<int:game_id>/assign_weakness/<int:weakness_id>/', views.assign_weakness, name='assign_weakness'),
    path('games/<int:game_id>/unassign_weakness/<int:weakness_id>/', views.unassign_weakness, name='unassign_weakness'),
    path('weakness/', views.WeaknessList.as_view(), name='weakness_index'),
    path('weakness/<int:pk>/', views.WeaknessDetail.as_view(), name='weakness_detail'),
    path('weakness/create/', views.WeaknessCreate.as_view(), name='weakness_create'),
    path('weakness/<int:pk>/update/', views.WeaknessUpdate.as_view(), name='weakness_update'),
    path('weakness/<int:pk>/delete/', views.WeaknessDelete.as_view(), name='weakness_delete'),
]