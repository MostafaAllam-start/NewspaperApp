from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'age', 'is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)