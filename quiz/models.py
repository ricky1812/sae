from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)
	currRounnd=models.IntegerField(default=1)

	def getHints():
		return currRounnd
        
@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Rounds(models.Model):
	round=models.IntegerField()
	question=models.CharField(max_length=500)
	ans=models.CharField(max_length=500)



