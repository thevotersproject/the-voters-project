from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        # if request.user.is_authenticated and request.user.is_staff:
        #     return redirect('/admins-dashboard')
        if request.user.is_authenticated:
            return redirect('/mainuser')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function
