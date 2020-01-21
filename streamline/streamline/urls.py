from django.contrib import auth, admin
from django.urls import include, path
from django.conf import settings 
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', include('mainsite.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', views.signup),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)