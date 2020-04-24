from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    read_only_fields = ('date_joined', 'last_login')
    ordering = ('email', 'first_name', 'last_name', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
