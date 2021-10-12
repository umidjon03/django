from django.contrib import admin
from .models import Message
from django.contrib.auth.admin import UserAdmin
from .forms import MesssageForm
# Register your models here.

class MessageAdmin(UserAdmin):
    form=Message
    form=MesssageForm

admin.site.register(Message)
