from django.shortcuts import render

# Create your views here.
def get_platform(request):
    return render(request, "third_task/platform.html")

def get_cart(request):
    return render(request, "third_task/cart.html")
def get_games(request):
    g1 = 'Atomik Heart'
    g2 = 'Cyberpunk 2077'
    g3 = 'PayDay2'
    context = {
        'g1': g1,
        'g2': g2,
        'g3': g3,
    }
    return render(request, "third_task/games.html", context=context)
