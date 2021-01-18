from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



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
    user = auth.authenticate(username=username.strip(), password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse("Success",status=200)

    else:
        return HttpResponse("Invalid login. Please try again.",status=401)

    return render(request, "login.html", {'next':'hello'})


def login_view(request):
	return render(request,'login.html')


def signup(request):
	data_list = []
	username = request.GET.get('username')
	if User.objects.filter(username =username.strip()).exists():
		return HttpResponse('username already exists,please choose a unique username',status=409)
	if username != None or '':
		data_list.append(username.strip())
	first_name = request.GET.get('first_name')
	if first_name != None or '':
		data_list.append(first_name.strip())
	last_name = request.GET.get('last_name')
	if last_name != None or '':
		data_list.append(last_name.strip())
	email = request.GET.get('email')
	if User.objects.filter(email = email.strip()).exists():
		return HttpResponse('email already exists,please choose a unique email',status=409)
	if email != None or '':
		data_list.append(email.strip())
	password =request.GET.get('password')
	data_list.append(password)
	password2 = request.GET.get('password2')
	data_list.append(password2)
	print(data_list)
	if password2 != password:
		return HttpResponse('password do not match',status=401)
	if len(data_list) !=6:
		return HttpResponse('Some fields data missing',status=500)
	else:
		User.objects.create(username=username.strip(),first_name=first_name.strip(),last_name=last_name.strip(),email=email.strip(),password=make_password(password))
		return HttpResponse('Success',status=200)

def signup_view(request):
	return render(request,'signup.html')

@login_required
def dashboard(request):
	return render(request,'dashboard.html')
