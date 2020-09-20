from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .user import User
from .models import Borrower, Loan, CreditProduct, Payments, Fee


class BorrowerInLine (admin.StackedInline):
    model = Borrower
    can_delete = False
    verbose_name_plural = 'borrower'


class UserAdmin(BaseUserAdmin):
    inlines = (BorrowerInLine, )


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'IsLoanOfficer')
    list_filter = ('username', 'email', 'first_name', 'last_name',  'is_staff', 'is_active','IsLoanOfficer')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'IsLoanOfficer')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',  'is_staff', 'is_active', 'IsLoanOfficer')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Loan),
admin.site.register(CreditProduct),
admin.site.register(Payments),
admin.site.register(Fee),



