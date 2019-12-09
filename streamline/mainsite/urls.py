from django.contrib import auth, admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products_index),
    path('accounts/', include('django.contrib.auth.urls')),
]