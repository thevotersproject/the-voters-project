from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user', views.user, name='user'),
    path('voter', views.voter, name='voter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
