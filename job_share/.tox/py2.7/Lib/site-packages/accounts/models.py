from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

# Create your models here.

#users = User.objects.all()
#User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pers_summary = models.TextField(max_length=500, blank=True)
    target_partner = models.TextField(max_length=500, default ='', blank=True)
    skills = models.TextField(max_length=200, default ='',blank=True)
    industry = models.TextField(max_length=50, default ='',blank=True)
    employed = models.TextField(max_length=3, default ='',blank=True)
    position = models.CharField(max_length=100, default ='',blank=True)
    years_exp = models.IntegerField(default = 0)


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
