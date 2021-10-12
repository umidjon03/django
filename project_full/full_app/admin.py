from django.contrib import admin
from .models import Login
from .forms import LoginForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class LoginAdmin(UserAdmin):
    form=LoginForm
    model=Login


admin.site.register(Login)