from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required #redirect when user is not logged in
def hello(request):
	return render(request,'index.html')

def login(request):
    '''Shows a login form and a registration link.'''

    username = request.GET.get('username')
    print(username)
    password = request.GET.get('password')
    print(password)
    print('hello')
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse("Success",status=200)

    else:
        return HttpResponse("Invalid login. Please try again.",status=401)

    return render(request, "login.html", {'next':'hello'})


def login_view(request):
	return render(request,'login.html')