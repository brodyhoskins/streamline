from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from mainsite.models import Vendor
from streamline.processors import vendor
from .forms import VendorForm

def index(request):
    return render(request, 'index.html')

def products_index(request):
    return render(request, 'products/index.html')

def vendor_index(request):
    if request.user.is_authenticated:
        if not vendor(request)['vendor'] == None:
            return render(request, 'vendors/index.html')
        else:
            return redirect('/vendors/signup')
    else:
        return render(request, '401.html', status = 401)

def vendor_signup(request):
    if request.user.is_authenticated:
        if not vendor(request)['vendor'] == None:
            return redirect('/vendors/')
        else:
            if request.method == 'POST':
                form = VendorForm(request.POST)
                if form.is_valid():
                    new_vendor = Vendor(name = form.cleaned_data['name'])
                    new_vendor.profile_id = request.user.id
                    new_vendor.save()
                    return redirect('/vendors/#welcome')
                else:
                    render(request, 'vendors/signup.html')
            else:
                form = VendorForm()
                return render(request, 'vendors/signup.html', {'form': form})
    else:
        return render(request, '401.html', status = 401)