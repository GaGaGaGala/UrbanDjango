from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(min_length=8, label='Пароль')
    repeat_password = forms.CharField(label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Ваш возраст')
    subscribe = forms.BooleanField(required=False, label='Зарегистрироваться')