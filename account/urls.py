from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainuser, name='mainuser'),
    path('event', views.event, name='event'),
    path('candidate', views.candidate, name='candidate'),
    path('voter', views.voter, name='voter'),
    path('editevent/<int:code>', views.editevent, name='editevent')
]
