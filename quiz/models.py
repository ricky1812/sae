from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)
	email=models.EmailField(max_length=70,null=True, unique=True)


	

	
        
@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Rounds(models.Model):
	curr_round=models.IntegerField(default=1)
	

	def __str__(self):
		return str(self.curr_round)

class Question(models.Model):
	question=models.CharField(max_length=500)
	ans=models.CharField(max_length=500,default=None)
	hint=models.CharField(max_length=500,default=None)
	round=models.ForeignKey(Rounds,on_delete=models.CASCADE)

	def __str__(self):
		return self.question






	






