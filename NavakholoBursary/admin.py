from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin', 'is_finance')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_admin', 'is_finance')}),
    )
    list_display = ('username', 'email', 'is_admin', 'is_finance')
    search_fields = ('username', 'email')
    ordering = ('-is_admin',)

admin.site.register(CustomUser, CustomUserAdmin)
