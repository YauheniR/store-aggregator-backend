from django.contrib.auth.models import AbstractUser
from django.db import models
from users.Constants import Language


class UserModel(AbstractUser):
    LANGUAGE_CHOICES = (
        ('RU', Language.RU),
        ('EN', Language.EN),
        ('BY', Language.BY),
    )

    city = models.CharField(max_length=25, blank=True, null=True,)
    address = models.CharField(max_length=150, blank=True, null=True,)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, blank=True, null=True,)
    date_of_birth = models.DateField(blank=True, null=True,)
