from django import forms
from .models import *

class CreateShoppingListForm(forms.Form):
    label = forms.CharField(max_length=255)