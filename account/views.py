from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from home.models import AdminProfile


# Create your views here.
def mainuser(request):
    if request.POST:
        profile = AdminProfile.objects.get(admin_id=1)
        return render(request, 'account/mainuser.html', {'profile': profile})
    profile = AdminProfile.objects.get(admin_id=1)
    return render(request, 'account/mainuser.html', {'profile': profile})


def event(request):
    events = EventTable.objects.filter(admin_id=1)
    return render(request, 'account/event.html', {'events': events})


def candidate(request):
    candidates = CandidateTable.objects.filter(admin_id=1)
    return render(request, 'account/candidate.html', {'candidates': candidates})


def voter(request):
    voters = VoterTable.objects.filter(admin_id=1)
    return render(request, 'account/voter.html', {'voters': voters})


def editevent(request, code):
    current_event = EventTable.objects.get(eventUUID=code)
    print(current_event)
    return render(request, 'account/editevent.html', {'current_event': current_event})
