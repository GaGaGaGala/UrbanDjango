"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task4.views import get_platform, get_games, get_cart, get_menu
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),
    path('task5/', include('task5.urls')),
    path('platform/', get_platform),
    path('platform/cart/', get_cart),
    path('platform/games/', get_games),
    path('menu/', get_menu),
    path('sign_up_html/', sign_up_by_html, name='sign_up_by_html'),
    path('sign_up_django/', sign_up_by_django, name='sign_up_by_django'),
 ]


