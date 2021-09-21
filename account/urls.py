from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainuser, name='mainuser'),
    path('event', views.event, name='event'),
    path('candidate', views.candidate, name='candidate'),
    path('voters', views.voter, name='voters'),
    path('editevent/<int:code>', views.edit_event, name='editevent'),
    path('delete_event/<int:code>', views.delete_event, name='delete_event'),
    path('addvoters', views.add_voter, name='add_voter'),
    path('delete_voter/<int:code>', views.delete_voter, name='delete_voter'),
    path('update_voter/<int:code>', views.update_voter, name='update_voter'),
    path('addcandidates', views.add_candidate, name='add_candidate'),
    path('delete_candidate/<int:code>', views.delete_candidate, name='delete_candidate'),
    path('update_candidate/<int:code>', views.update_candidate, name='update_candidate'),
    path('addevents', views.add_event, name='add_event'),
]
