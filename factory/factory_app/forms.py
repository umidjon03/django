from .models import Message
from django import forms

class MesssageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['name','phone','location','email','message','emailcopy','human']