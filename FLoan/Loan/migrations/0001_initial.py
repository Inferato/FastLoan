# Generated by Django 3.1 on 2020-09-13 15:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('DOB', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('net_income', models.FloatField(default=0)),
                ('ssn', models.CharField(max_length=8)),
                ('IDCard', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='CreditProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('maxAmount', models.FloatField(default=1)),
                ('minAmount', models.FloatField(default=1)),
                ('maxTerm', models.IntegerField(default=1)),
                ('minTerm', models.IntegerField(default=1)),
                ('minNetIncome', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeeAmount', models.FloatField(default=0)),
                ('FeeUsage', models.CharField(choices=[('E', 'Every payment'), ('F', 'First payment'), ('L', 'Last payment')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('DateOfDisburse', models.DateField(default=datetime.date.today, null=True)),
                ('DateOfClose', models.DateField(default=datetime.date.today, null=True)),
                ('IsActive', models.BooleanField(default=False)),
                ('TotalToPay', models.FloatField(default=0)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loan.borrower')),
                ('credit_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Loan.creditproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfPayment', models.DateField()),
                ('PaymentAmount', models.FloatField(default=0)),
                ('FeePaid', models.FloatField(default=0)),
                ('Loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loan.loan')),
            ],
        ),
        migrations.AddField(
            model_name='creditproduct',
            name='fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Loan.fee'),
        ),
    ]