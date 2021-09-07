from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from home.models import AdminProfile


# Create your views here.
def mainuser(request):
    profile = AdminProfile.objects.filter(admin_id=1)
    return render(request, 'account/mainuser.html', {'profile': profile})


def event(request):
    events = EventTable.objects.filter(admin_id=1)
    return render(request, 'account/event.html', {'events': events})


def candidate(request):
    candidates = CandidateTable.objects.filter(admin_id=1)
    return render(request, 'account/candidate.html', {'candidates': candidates})


def user(request):
    users = UserTable.objects.filter(admin_id=1)
    return render(request, 'account/user.html', {'users': users})
