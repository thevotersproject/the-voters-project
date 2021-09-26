from django.contrib import auth, messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from home.models import AdminProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def mainuser(request):
    user = request.user
    profile = AdminProfile.objects.get(admin_id=user.id)
    if request.method == "POST":
        form = User(instance=request)
        profileForm = AdminProfile()

        form.first_name = request.POST['firstname']
        form.last_name = request.POST['lastname']

        profileForm.role = request.POST['role']
        profileForm.bio = request.POST['bio']

        # return render(request, 'account/mainuser.html', {'profile': profile})
    return render(request, 'account/mainuser.html', {'profile': profile})


@login_required(login_url='login')
def event(request):
    user = request.user
    events = EventTable.objects.filter(admin_id=user.id)
    return render(request, 'account/event.html', {'events': events})


@login_required(login_url='login')
def candidate(request):
    user = request.user
    candidates = CandidateTable.objects.filter(admin_id=user.id)
    return render(request, 'account/candidate.html', {'candidates': candidates})


@login_required(login_url='login')
def voter(request):
    user = request.user
    voters = VoterTable.objects.filter(admin_id=user.id)
    return render(request, 'account/voter.html', {'voters': voters})


@login_required(login_url='login')
def event_delete_voter(request, voters):
    pass


@login_required(login_url='login')
def unselect_candidate(request, candidates):
    user = request.user
    current_event = EventTable.objects.get(id=candidates)


@login_required(login_url='login')
def edit_event(request, code):
    user = request.user
    current_event = EventTable.objects.get(id=code)
    candidates = []
    voters = []
    if request.method == 'POST':
        now_voters = request.POST.getlist('current_voters')
        now_candidates = request.POST.getlist('current_candidates')
        if now_voters:
            for i in now_voters:
                add = VoterEvent()
                add.event_id = code
                add.voter_id = int(i)
                try:
                    add.save()
                    messages.success(request, "Voters Added to the Event")
                except Exception as e:
                    messages.error(request, "Duplicate Voter")
                    print(e)

        if now_candidates:
            for i in now_candidates:
                add = CandidateEvent()
                add.event_id = code
                add.candidate_id = int(i)
                try:
                    add.save()
                    messages.success(request, "Candidates Added to the Event")
                except Exception as e:
                    messages.error(request, "Duplicate Candidates")
                    print(e)

    if request.POST.get('remove_candidate'):
        remove_candidate = request.POST.getlist('remove_candidates')
        if remove_candidate:
            for i in remove_candidate:
                deleteCandidate = current_event.candidateevent_set.get(candidate_id=int(i), event_id=code)
                deleteCandidate.delete()

    if request.POST.get('remove_voter'):
        remove_voter = request.POST.getlist('remove_voters')
        if remove_voter:
            for i in remove_voter:
                deleteVoter = current_event.voterevent_set.get(voter_id=int(i), event_id=code)
                deleteVoter.delete()

    for i in CandidateEvent.objects.filter(event_id=code):
        candidates.append(CandidateTable.objects.get(id=i.candidate_id))

    for i in VoterEvent.objects.filter(event_id=code):
        voters.append(VoterTable.objects.get(id=i.voter_id))

    current_candidates = CandidateTable.objects.filter(admin_id=user.id)  # send candidates for this event. with event
    current_voters = VoterTable.objects.filter(admin_id=user.id)

    return render(request, 'account/editevent.html',
                  {'current_event': current_event, 'current_candidates': current_candidates,
                   'current_voters': current_voters, 'candidates': candidates, 'voters': voters})


@login_required(login_url='login')
def delete_event(request, code):
    user = request.user
    current_event = EventTable.objects.get(id=code)
    if request.method == 'POST':
        current_event.delete()
        return redirect('event')
    return redirect('event')


@login_required(login_url='login')
def add_voter(request):
    user = request.user
    if request.method == 'POST':
        form = VoterTable()
        form.admin_id = user.id
        form.voterFirstname = request.POST.get('firstname')
        form.voterLastname = request.POST.get('lastname')
        form.voterFingerprint = request.POST.get('fingerprint')
        form.voterImg = request.FILES['image']
        try:
            form.save()
            messages.success(request, "Voter created")
        except IntegrityError:
            messages.error(request, "Voter exists with this fingerprint")

    context = {}

    return render(request, 'account/add_voter.html', context)


@login_required(login_url='login')
def update_voter(request, code):
    user = request.user
    pass


@login_required(login_url='login')
def delete_voter(request, code):
    user = request.user
    pass


@login_required(login_url='login')
def add_candidate(request):
    user = request.user
    if request.method == 'POST':
        form = CandidateTable()
        form.admin_id = user.id
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


@login_required(login_url='login')
def update_candidate(request, code):
    user = request.user
    print(code)


@login_required(login_url='login')
def delete_candidate(request, code):
    user = request.user
    pass


@login_required(login_url='login')
def add_event(request):
    user = request.user
    if request.method == 'POST':
        form = EventTable()
        form.admin_id = user.id
        form.eventName = request.POST.get('eventName')
        form.eventDetails = request.POST.get('eventDetails')
        form.eventPosition = request.POST.get('eventPosition')
        form.eventStartDate = request.POST.get('start_date')
        form.eventEndDate = request.POST.get('end_date')

        try:
            form.save()
            print("check")
            messages.success(request, "Event Added")
        except Exception as e:
            print(e)

    return render(request, 'account/add_event.html')
