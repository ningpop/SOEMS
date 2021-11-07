from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    ''' User admin Custom '''

    fieldsets = (
        (None, {"fields": ("username", "password", "name", "phone", "email")},
        ),
    )

    list_display = (
        "username",
        "name",
        "email",
        "phone",
    )