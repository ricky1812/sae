from django.shortcuts import render,HttpResponse,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
from .models import Profile,Rounds



# Create your views here.
def index(request):
	return HttpResponse("This is the homepage")

def signup(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Registered Succesfully")
	else:
		form=RegistrationForm()
	args={'form': form}
	return render(request,'quiz/signup.html',args)

def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('index')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'quiz/login.html',context)
def logout(request):
	logout(request)
	return redirect('index')
def logout(request):
	logout(request)
	return redirect('index')

def leaderboard(request):
	people=[]
	profiles = Profile.objects.all()
	for i in profiles:
		myuser = User.objects.get(id=i.user_id)
		people.append({
			'username':myuser.username,
			'score':i.score,
			})
	return render(request,'quiz/leaderboard.html',{'people':people})

def get_question(request):
	
	user=User.objects.get(username=request.user.username)
	
	
	return render(request,'quiz/quizpage.html',{'user':user})


	
			
        
	




