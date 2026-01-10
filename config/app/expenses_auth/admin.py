from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "username",
        "email",
        "mobile_number",
        "is_staff",
        "is_active",
    )
    search_fields = ("username", "email", "mobile_number")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "mobile_number", "address"),
        }),
    )
