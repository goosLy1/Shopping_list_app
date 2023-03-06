from django import forms
from .models import *

class CreateShoppingListForm(forms.ModelForm):
    class Meta:
        model = Shopping_list
        fields = ['label']


class CreateProductForm(forms.Form):
    label = forms.CharField(max_length=255)
    price = forms.FloatField(min_value=0, max_value=100000)