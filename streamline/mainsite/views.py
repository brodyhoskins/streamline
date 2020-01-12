from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def products_index(request):
    return render(request, 'products/index.html')