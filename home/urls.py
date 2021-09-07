from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voter', views.voter, name='voter'),
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
    path('mainuser/', include('account.urls'), name='mainuser'),
    path('logout', views.logout, name='logout'),
]
