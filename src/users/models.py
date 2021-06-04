from django.contrib.auth.models import AbstractUser
from django.db import models
from core.settings import LANGUAGE_CODE


class UserModel(AbstractUser):
    city = models.CharField(max_length=25, blank=True, null=True,)
    address = models.CharField(max_length=150, blank=True, null=True,)
    language = models.CharField(default=LANGUAGE_CODE, max_length=20, blank=True, null=True,)
    date_of_birth = models.DateField(blank=True, null=True,)
