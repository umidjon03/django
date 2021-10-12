from django.contrib import admin
from .models import Message

from .forms import MessageForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class LoginAdmin(UserAdmin):
    form=MessageForm
    model=Message

admin.site.register(Message)