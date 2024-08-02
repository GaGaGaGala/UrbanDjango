from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def sign_up_by_html(request):
    users = []
    info = {}
    context = {
        'users': users,
        'info': info,
}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        subscribe = request.POST.get('subscribe') == 'on'

        print(f"Username:{username}")
        print(f"Password:{password}")
        print(f"repeat_password:{repeat_password}")
        print(f"age:{age}")
        print(f"Subscribe:{subscribe}")


        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
        return HttpResponse(f'Приветствуем, truelogin!')
    return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_django(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            subscribe = form.cleaned_data['subscribe']
        return HttpResponse(f'Приветствуем, truelogin!')

    else:
        form = ContactForm()
    return render(request, 'fifth_task/registration_page.html', {'form': form})
