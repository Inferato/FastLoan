# Generated by Django 3.1 on 2020-09-16 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrower',
            old_name='SSN',
            new_name='ssn',
        ),
    ]