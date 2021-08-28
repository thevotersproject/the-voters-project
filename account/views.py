from django.shortcuts import render


# Create your views here.
def mainuser(request):
    return render(request, 'account/mainuser.html')
