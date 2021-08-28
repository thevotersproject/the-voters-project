from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voter', views.voter, name='voter'),
    path('register', views.register, name='register'),
    path('login', include('account.urls')),
]
