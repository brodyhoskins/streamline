from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extend User model to simulate custom attributes
# Advice from <https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone>
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Vendor(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    profile = models.OneToOneField(Profile, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    vendors = models.ManyToManyField(Vendor)
    title = models.CharField(max_length = 255)
    desc = models.TextField()

class PreferredProduct(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    ship_by = models.DateTimeField()
    products = models.ManyToManyField(Product)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()