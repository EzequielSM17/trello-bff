from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
         'fields': ('first_name', 'last_name', 'username')}),
        (
            _('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important Dates'), {'fields': ('last_login',), }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password1')
        }
        ),
    )


admin.site.register(User, UserAdmin)
