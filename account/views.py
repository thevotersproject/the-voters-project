from django.contrib import auth, messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from home.models import AdminProfile


# from .forms import *


# Create your views here.
def mainuser(request):
    profile = AdminProfile.objects.get(admin_id=1)
    if request.POST:
        form = User()
        profileForm = AdminProfile()

        form.first_name = request.POST['firstname']
        form.last_name = request.POST['lastname']
        profileForm.role = request.POST['role']
        profileForm.bio = request.POST['bio']
        return render(request, 'account/mainuser.html', {'profile': profile})
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


def edit_event(request, code):
    current_event = EventTable.objects.get(id=code)
    candidates = CandidateTable.objects.filter(admin_id=1)
    voters = VoterTable.objects.filter(admin_id=1)

    return render(request, 'account/editevent.html', {'current_event': current_event,
                                                      'candidates': candidates,
                                                      'voters': voters})


def add_voter(request):
    # form = VoterForm()
    if request.method == 'POST':
        form = VoterTable()
        form.admin_id = 1
        form.voterFirstname = request.POST.get('firstname')
        form.voterLastname = request.POST.get('lastname')
        form.voterFingerprint = request.POST.get('fingerprint')
        form.voterImg = request.FILES['image']
        try:
            form.save()
            messages.success(request, "Voter created")
        except IntegrityError:
            messages.error(request, "Voter exists with this fingerprint")
        # print(form.voterFingerprint)
        # if form.is_valid():

    context = {}

    return render(request, 'account/add_voter.html', context)


def add_candidate(request):
    if request.method == 'POST':
        form = CandidateTable()
        form.admin_id = 1
        form.candidateFirstname = request.POST.get('firstname')
        form.candidateLastname = request.POST.get('lastname')
        form.candidateDetails = request.POST.get('details')
        form.candidateImg = request.FILES['image']

        try:
            form.save()
            messages.success(request, "Candidate Added")
        except Exception as e:
            messages.error(request, e)

    context = {}
    return render(request, 'account/add_candidate.html', context)


def add_event(request):
    if request.method == 'POST':
        pass
        # form = EventForm(request.POST)
        # if form.is_valid():
        #     form.save()

    context = {}

    return render(request, 'account/add_event.html', context)
