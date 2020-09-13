from django.db import models


class CreditProduct(models.Model):
    name = models.CharField(max_length=200)
    maxAmount = models.FloatField()
    minAmount = models.FloatField()
    maxTerm = models.IntegerField()
    minTerm = models.IntegerField()
    minNetIncome = models.FloatField()


class Borrower(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField()
    net_income = models.FloatField()
    ssn = models.CharField()
    IDCard = models.CharField()


class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.FloatField()
    DateOfDisburse = models.DateField()
    DateOfClose = models.DateField()
    IsActive = models.BooleanField()
    TotalToPay = models.FloatField()


class Payments(models.Model):
    Loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    DateOfPayment = models.DateField()
    PaymentAmount = models.FloatField()
    FeePaid = models.FloatField()


class Fee(models.Model):
    creditprod = models.ForeignKey(CreditProduct, on_delete=models.CASCADE)
    FeeAmount = models.FloatField()
    FeeUsage = models.CharField()