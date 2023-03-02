from django import forms
from .models import *

class CreateShoppingListForm(forms.Form):
    label = forms.CharField(max_length=255)


class CreateProductForm(forms.Form):
    label = forms.CharField(max_length=255)
    price = forms.FloatField()