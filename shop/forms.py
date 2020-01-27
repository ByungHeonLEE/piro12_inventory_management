from django import forms
from .models import Product
from .models import Client


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
