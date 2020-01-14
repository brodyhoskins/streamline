from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products_index),
    path('vendors/', views.vendor_index),
    path('vendors/signup', views.vendor_signup),
]