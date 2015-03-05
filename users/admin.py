from __future__ import absolute_import

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserSignUpForm, UserChangeForm

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserSignUpForm

    list_display = ('email', 'username', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': (
            'email', 'username', 'slug', 'is_superuser', 'is_active'
        )}),
#        ('Following', {'fields': ('following',)}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': {'email', 'username', 'password1', 'password2'}
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups',)

admin.site.register(User, CustomUserAdmin)
