from django import contrib
from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

# Register your models here.


class AccountAdmin(UserAdmin):
    ordering = ['date_joined']
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ['last_name', 'username']
    search_fields = ['last_name', 'first_name', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('last_name', 'first_name', 'username')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superadmin', 'is_admin')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(Account, AccountAdmin)
