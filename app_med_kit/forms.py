from django import forms
from .models import Kit

class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ['name', 'description']

from .models import Drug

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'number', 'description', 'price', 'expiration_date']