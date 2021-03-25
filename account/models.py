from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=35)
    username = models.CharField(max_length=15)
    date_joined = models.DateField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateField(verbose_name="last login",auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
