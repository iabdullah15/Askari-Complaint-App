from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    designation = models.CharField(default='Resident', max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'designation']

    def __str__(self):
        return self.email