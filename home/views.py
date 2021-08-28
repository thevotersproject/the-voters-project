from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')


def user(request):
    return render(request, 'user.html')


def voter(request):
    if request.method == "POST":
        code = request.POST['event_code']
        print(code)
    return render(request, 'voter.html')


def login(request):
    return redirect('login/mainuser')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
    return render(request, 'register.html')
