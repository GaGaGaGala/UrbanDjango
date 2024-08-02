from django.urls import path
from . import views

urlpatterns = [
    path('sign_up_html/', views.sign_up_by_html, name='sign_up_by_html'),
    path('sign_up_django/', views.sign_up_by_django, name='sing_up_by_django'),
]
