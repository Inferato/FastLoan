from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Borrower, Loan, CreditProduct, Payments, Fee, LoanOfficer


class BorrowerInLine (admin.StackedInline):
    model = Borrower
    can_delete = False
    verbose_name_plural = 'borrower'


class LoanOfficerInLine(admin.StackedInline):
    model = LoanOfficer
    can_delete = False
    verbose_name_plural = 'loan officer'


class UserAdmin(BaseUserAdmin):
    inlines = (BorrowerInLine, LoanOfficerInLine,)


# Register your models here.
admin.site.register(Loan),
admin.site.register(CreditProduct),
admin.site.register(Payments),
admin.site.register(Fee),
admin.site.unregister(User)
admin.site.register(User, UserAdmin)