from django.contrib.auth.models import AbstractUser
from django.db import models
from users.constants import LanguageEnum


class UserModel(AbstractUser):
    LANGUAGE_CHOICES = (
        ('RU', LanguageEnum.RU),
        ('EN', LanguageEnum.EN),
        ('BY', LanguageEnum.BY),
    )

    city = models.CharField(max_length=25, blank=True, null=True,)
    address = models.CharField(max_length=150, blank=True, null=True,)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, blank=True, null=True,)
    date_of_birth = models.DateField(blank=True, null=True,)
