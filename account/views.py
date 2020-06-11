from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def registration(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		usertype = request.POST.get('usertype')

		user = User.objects.create_user(username=username,email=email,password=password)
		user.profile.usertype = usertype
		user.save()
		print(user)
		return redirect('index')
	else:
		return render(request,'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			print(user.profile.usertype)

			return redirect('index')
	else:


		return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')