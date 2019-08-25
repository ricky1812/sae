from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)
	curr_round=models.IntegerField(default=1)
	submit_time =  models.DateTimeField(auto_now_add=True)


	

	
        
@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Question(models.Model):
	question=models.CharField(max_length=500)
	ans=models.CharField(max_length=500,default=None)
	hint=models.CharField(max_length=500,default=None)
	image = models.ImageField(upload_to='images',default="Not Available", blank=True)
	round=models.IntegerField(default=1)

	def __str__(self):
		return self.question






	






