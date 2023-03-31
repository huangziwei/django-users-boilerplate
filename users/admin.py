from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm

# from .models import CustomUser

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "name", "is_superuser"]
    search_fields = ["email", "username", "name"]
    form = UserChangeForm
    add_form = UserCreationForm
