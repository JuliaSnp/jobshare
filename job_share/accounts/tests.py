from django.test import TestCase
from accounts.models import UserProfile

# Create your tests here.

#The tutorial used when writing this test: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

#class UserProfileModelTest(TestCase):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    pers_summary = models.TextField(max_length=500, blank=True)
#    target_partner = models.TextField(max_length=500, default ='', blank=True)
#    skills = models.TextField(max_length=200, default ='',blank=True)
#    industry = models.TextField(max_length=50, default ='',blank=True)
#    employed = models.TextField(max_length=3, default ='',blank=True)
#    position = models.CharField(max_length=100, default ='',blank=True)
#    years_exp = models.IntegerField(default = 0)
