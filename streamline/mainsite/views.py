from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from streamline.processors import vendor

def index(request):
    return render(request, 'index.html')

def products_index(request):
    return render(request, 'products/index.html')

def vendor_index(request):
    if request.user.is_authenticated:
        if vendor == True:
            return render(request, 'vendors/index.html')
        else:
            return redirect('/vendors/signup')
    else:
        return render(request, '401.html', status = 401)

def vendor_signup(request):
    if request.user.is_authenticated:
        if vendor == True:
            return redirect('/vendors/')
        else:
            return render(request, 'vendors/signup.html')
    else:
        return render(request, '401.html', status = 401)