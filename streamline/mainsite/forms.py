from django import forms

class VendorForm(forms.Form):
    name = forms.CharField(label = 'Company', max_length = 100)