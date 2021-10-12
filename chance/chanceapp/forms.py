from django.forms import fields
from chanceapp.models import Admin
from .models import  Opinion,Admin
from django import forms

class OpinionForm(forms.ModelForm):
    class Meta:
        model=Opinion
        fields=['name','email','message']

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=['name','email','phone_number']