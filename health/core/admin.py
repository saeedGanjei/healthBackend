from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users """
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'address',
                    'phone_number', 'created_at', 'image',]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'created_at')}),
        (_('Contacts'), {'fields': ('phone_number', 'address', 'image')})
    )
    readonly_fields = ['last_login', 'created_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'is_active',
                'is_staff',
                'is_superuser',
                'address',
                'phone_number',
                'image',
            )
        }),
    )


admin.site.register(User, UserAdmin)
