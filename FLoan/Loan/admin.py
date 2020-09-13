from django.contrib import admin
from .models import Borrower, Loan, CreditProduct, Payments, Fee

# Register your models here.
admin.site.register(Borrower),
admin.site.register(Loan),
admin.site.register(CreditProduct),
admin.site.register(Payments),
admin.site.register(Fee),
