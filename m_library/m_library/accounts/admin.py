from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from m_library.accounts.forms import UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class MLibraryUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)
