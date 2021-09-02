from django.shortcuts import render, redirect
from .forms import AdminRegisterForm, AdminProfileForm
from django.contrib import messages


# Create your views here.
def home(request):
    imgs = ['c-logo-1.png', 'c-logo-2.png', 'c-logo-3.png', 'c-logo-4.png', 'c-logo-5.png']
    return render(request, 'home/index.html', {'imgs': imgs})


def voter(request):
    if request.method == "POST":
        code = request.POST['event_code']
        print(code)
    return render(request, 'home/voter.html')


def login(request):
    return render(request, 'home/login.html')


def register(request):
    if request.method == "POST":
        form = AdminRegisterForm(request.POST)
        profile_form = AdminProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.admin = user

            profile.save()

            username = form.cleaned_data['username']
            messages.success(request, f'Admin Created for {username}')
            return redirect('home')
        # else:
        #     j = ''
        #     for i in form:
        #         for j in i.errors:
        #             print(j)
        #     messages.error(request, j)
    else:
        form = AdminRegisterForm()
        profile_form = AdminProfileForm(request.POST)

    return render(request, 'home/register.html', {'form': form, 'profile': profile_form})
