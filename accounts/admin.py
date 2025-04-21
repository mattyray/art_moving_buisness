from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ("email", "username", "is_superuser")
    list_filter  = ("is_superuser", "is_staff", "is_active")

    search_fields = ("email", "username")
    ordering      = ("email",)

    # Edit form layout
    fieldsets = (
        (None,               {"fields": ("email", "username", "password")}),
        ("Permissions",      {"fields": ("is_active", "is_staff", "is_superuser",
                                         "groups", "user_permissions")}),
        ("Important dates",  {"fields": ("last_login", "date_joined")}),
    )

    # Add form layout (uses Django's built‑in password1/password2 fields)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2",
                       "is_active", "is_staff"),
        }),
    )
