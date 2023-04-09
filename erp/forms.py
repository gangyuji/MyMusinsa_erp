
 

from django import forms
from .models import ProductModel, InBound, OutBound, Inventory

# form


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'code', 'description', 'price', 'size']


class InBoundForm(forms.ModelForm):
    class Meta:
        model = InBound
        fields = ['amount', 'cost', 'code_name_size']


class OutBoundForm(forms.ModelForm):
    class Meta:
        model = OutBound
        fields = ['amount', 'cost', 'code_name_size']