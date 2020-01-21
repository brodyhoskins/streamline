from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from mainsite.models import Product, Vendor
from streamline.processors import vendor
from .forms import ProductForm, VendorForm

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_new(request):
    if request.user.is_authenticated:
        if not vendor(request)['vendor'] == None:
            if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    product = form.save(commit = False)
                    product.title = form.cleaned_data['title']
                    product.desc = form.cleaned_data['desc']
                    product.price = form.cleaned_data['price']
                    print(request.FILES['primary_image'])
                    product.primary_image = request.FILES['primary_image']
                    product.save()
                    product.vendors.add(vendor(request)['vendor'])
                    return redirect(f'/products/{product.pk}')
            form = ProductForm()
            return render(request, 'products/new.html', {'form': form})
    return render(request, '401.html', status = 401)

def products_edit(request, pk):
    if request.user.is_authenticated:
        if not vendor(request)['vendor'] == None:
            product = Product.objects.get(pk = pk)
            form = ProductForm(request.POST or None, instance = product)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    return redirect(f'/products/{product.pk}')
            return render(request, 'products/edit.html', {'form': form, 'product': product})
    return render(request, '401.html', status = 401)

def products_delete(request, pk):
    if request.user.is_authenticated:
        if not vendor(request)['vendor'] == None:
            if request.method == 'DELETE' or request.method == 'POST':
                Product.objects.get(pk = pk).delete()
                return redirect(f'/products')
            return render(request, '405.html', status = 405)
    return render(request, '401.html', status = 401)

def products_show(request, pk):
    product = Product.objects.get(pk = pk)
    vendor_names = ', '.join(list(product.vendors.values_list('name', flat = True)))
    return render(request, 'products/show.html', {'product': product, 'vendor_names': vendor_names})

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
            form = VendorForm()
            return render(request, 'vendors/signup.html', {'form': form})
    return render(request, '401.html', status = 401)