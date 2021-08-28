from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def voter(request):
    if request.method == "POST":
        code = request.POST['event_code']
        print(code)
    return render(request, 'home/voter.html')


def login(request):
    pass


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
    return render(request, 'home/register.html')
