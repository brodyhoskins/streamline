from django.contrib import auth, admin
from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', include('mainsite.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', views.signup),
]
