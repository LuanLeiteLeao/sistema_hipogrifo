from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','nome','cpf','tipo','matriz','is_pendente')
    list_filter = ('email', 'is_staff', 'is_active','nome','cpf','tipo','matriz','is_pendente')
    fieldsets = (
        (None, {'fields': ('email', 'password','nome','cpf','tipo','matriz','is_pendente')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','nome','cpf','tipo','matriz','is_pendente')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)