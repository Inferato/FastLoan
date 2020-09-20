from django.db import models
from .user import User
from datetime import date


class Fee(models.Model):
    FEE_TYPE = (
        ('E', 'Every payment'),
        ('F', 'First payment'),
        ('L', 'Last payment')
    )
    FeeAmount = models.FloatField(default=0)
    FeeUsage = models.CharField(max_length=1, choices=FEE_TYPE)

    def __str__(self):
        return 'Fee amount: {}'.format(self.FeeAmount) + \
               '\nUse for: {}'.format(self.FeeUsage)


class CreditProduct(models.Model):
    name = models.CharField(max_length=200)
    maxAmount = models.FloatField(default=1)
    minAmount = models.FloatField(default=1)
    maxTerm = models.IntegerField(default=1)
    minTerm = models.IntegerField(default=1)
    minNetIncome = models.FloatField(default=0)
    fee = models.ForeignKey(Fee, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.name) + \
               "\nMinimum allowed sum: {}".format(self.minAmount) + \
               "\nMaximum allowed sum: {}".format(self.maxAmount) + \
               "\nMinimum allowed term: {}".format(self.maxTerm) + \
               "\nMaximum allowed term: {}".format(self.maxTerm) + \
               "\nMinimal allowed net income: {}".format(self.minNetIncome)


class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField(default=date.today, null=True, blank=True)
    net_income = models.FloatField(default=0)
    ssn = models.CharField(max_length=8)
    IDCard = models.CharField(max_length=8)

    def __str__(self):
        now = date.today()
        return 'Borrower full name: {}'.format(str(self.name) + str(self.last_name)) + \
               '\nDate of birth: {}'.format(self.DOB) + \
               '\nAge: {}'.format((now.year - self.DOB.year)) + \
               '\nNet income: {}'.format(self.net_income) + \
               '\nSSN: {}'.format(self.ssn) + \
               '\nID Card: {}'.format(self.IDCard)


class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    credit_product = models.ForeignKey(CreditProduct, on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0)
    DateOfDisburse = models.DateField(default=date.today, null=True)
    DateOfClose = models.DateField(default=date.today, null=True)
    IsActive = models.BooleanField(default=False)
    TotalToPay = models.FloatField(default=0)
    Decision = models.CharField(max_length=15, null=True, blank=True)
    ClientDecision = models.BooleanField(default=True)
    DecisionMadeBy = models.CharField(max_length=200, null=True, blank=True)


class Payments(models.Model):
    Loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    DateOfPayment = models.DateField()
    PaymentAmount = models.FloatField(default=0)
    FeePaid = models.FloatField(default=0)
