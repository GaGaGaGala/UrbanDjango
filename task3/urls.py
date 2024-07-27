from django.urls import path
from . import views
urlpatterns = [
    path('cart/', views.get_cart, name='get_cart'),
    path('games/', views.get_games, name='get_games'),
    path('platform/', views.get_cart, name='get_platform'),
]