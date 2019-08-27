from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from . import models
from django.contrib.auth.models import User
from .models import Profile,Question
from django.utils import timezone
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
	return render(request,'quiz/index.html')
def index2(request):
	return render(request,'quiz/index2.html')

def signup(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
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
				return redirect('index2')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'quiz/login1.html',context)
@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
	


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
@login_required
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
	if user.profile.curr_round<=5:

		return render(request,'quiz/quizpage.html',{'round':round})
	else:
		return render(request,'quiz/endpage.html')
@login_required
def end_page(request):
	return render(request,'quiz/endpage.html')



	
			
        
	




