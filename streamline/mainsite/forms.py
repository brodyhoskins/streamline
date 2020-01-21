from django import forms
from mainsite.models import Product, Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name',)
    name = forms.CharField(label = 'Company', max_length = 100)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'desc', 'primary_image')
    title = forms.CharField(label = 'Title', max_length = 100)
    desc = forms.CharField(label = 'Description', max_length = 1024)
    price = forms.CharField(label = 'Price $', max_length = 6)
    primary_image = forms.ImageField()