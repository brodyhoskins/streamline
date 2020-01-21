from django import forms

class VendorForm(forms.Form):
    name = forms.CharField(label = 'Company', max_length = 100)

class ProductForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length = 100)
    desc = forms.CharField(label = 'Description', max_length = 1024)