from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from mainsite.models import *

def index(request):
    return render(request, 'index.html')

def products_index(request):
    return render(request, 'products/index.html')

def vendor_index(request):
    if request.user.is_authenticated:
        if Vendor.objects.filter(profile_id = request.user.profile.id):
            args = {}
            args['vendor'] = Vendor.objects.get(profile_id = request.user.profile.id)
            return render(request, 'vendors/index.html', args)
        else:
            return redirect('/vendors/signup')
    else:
        return render(request, '401.html', status = 401)

def vendor_signup(request):
    if request.user.is_authenticated:
        if Vendor.objects.filter(profile_id = request.user.profile.id):
            return redirect('/vendors/')
        else:
            return render(request, 'vendors/signup.html')
    else:
        return render(request, '401.html', status = 401)