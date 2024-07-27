from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def get_platform(request):
    return render(request, "fourth_task/platform.html")
def get_cart(request):
    return render(request, "fourth_task/cart.html")
def get_games(request):
    games = ["Atomic Heart", "Cyberpunk 2077", 'PayDay2']
    context = {
        'games': games,
    }
    return render(request, "fourth_task/games.html", context=context)
def get_menu(request):
    return render(request, "fourth_task/menu.html")
# Create your views here.
