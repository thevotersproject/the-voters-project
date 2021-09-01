from django.shortcuts import render, redirect
from .forms import AdminRegisterForm
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
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Admin Created for {username}')
            form.save()
            return redirect('home')
    else:
        form = AdminRegisterForm()
    return render(request, 'home/register.html', {'form': form})
