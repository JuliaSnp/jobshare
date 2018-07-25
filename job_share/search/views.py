from django.shortcuts import render
from django.contrib.auth.models import User
from .filters import UserFilter


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})

# Create your views here.
