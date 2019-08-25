from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
from .models import Profile,Question
from django.utils import timezone



# Create your views here.
def index(request):
	return render(request,'quiz/index.html')

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
def signout(request):
	logout(request)
	url = reverse(":login")
	return redirect(url, args=(),kwargs={}) 


def leaderboard(request):
	people=[]
	profiles = Profile.objects.order_by("-score","submit_time")
	for i in profiles:
		myuser = User.objects.get(id=i.user_id)
		people.append({
			'username':myuser.username,
			'score':i.score,
			'time':i.submit_time,
			})
	return render(request,'quiz/leaderboard.html',{'people':people})

def get_question(request):
	
	user=User.objects.get(username=request.user.username)
	round=Question.objects.get(round=user.profile.curr_round)
	
	if request.method=='POST':
		answers=request.POST['answers']
		print(answers)
		
		if answers==round.ans:
			print("correct")
			user.profile.curr_round+=1
			print(user.profile.curr_round)
			user.profile.score+=10
			user.profile.submit_time=timezone.now()
			print(user.profile.submit_time)
			user.save()	
			if user.profile.curr_round>=5:
				return redirect('end_page')
			else:

				return redirect('get_question')
	return render(request,'quiz/quizpage.html',{'round':round})

def end_page(request):
	return render(request,'quiz/endpage.html')



	
			
        
	




