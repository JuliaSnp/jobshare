"""job_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views
from django.urls import include, path
from job_share import views
from django.conf import settings
import debug_toolbar


urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^$', views.login_redirect, name = 'login_redirect'),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', )),
    url(r'^search/', include('search.urls', )),
    url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),

]
