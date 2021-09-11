from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainuser, name='mainuser'),
    path('event', views.event, name='event'),
    path('candidate', views.candidate, name='candidate'),
    path('voters', views.voter, name='voters'),
    path('editevent/<int:code>', views.edit_event, name='editevent'),
    path('addvoters', views.add_voter, name='add_voter'),
    path('addcandidates', views.add_candidate, name='add_candidate'),
    path('addevents', views.add_event, name='add_event'),
]
