from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    IsLoanOfficer = models.BooleanField(default=False)