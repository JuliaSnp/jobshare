from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfile
#from .filters import UserFilter
from .filters import ProfileFilter
from accounts.views import view_profile, view_profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def search(request):
                    #user_list = User.objects.all()
     user_list = UserProfile.objects.all()
                    #user_filter = UserFilter(request.GET, queryset=user_list)
     userprofile_filter = ProfileFilter(request.GET, queryset=user_list)
     return render(request, 'search/user_list.html', {'filter': userprofile_filter})
