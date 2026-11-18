from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'display_name', 'is_staff')
    list_filter = ('role',)
    search_fields = ('username', 'email', 'display_name')
    fieldsets = UserAdmin.fieldsets + (
        ('FretFlow', {'fields': ('role', 'display_name', 'contact_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('FretFlow', {'fields': ('role', 'display_name', 'contact_number')}),
    )
