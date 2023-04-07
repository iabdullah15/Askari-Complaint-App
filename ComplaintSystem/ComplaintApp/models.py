from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

from django.core.validators import MinValueValidator, MaxValueValidator


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
    

class Building(models.Model):

    SECTOR_CHOICES = (('A', 'SECTOR A'), ('B', 'SECTOR B'), ('C', 'SECTOR C'))

    BuildingNo = models.PositiveIntegerField(unique=True, primary_key=True)
    sector = models.CharField(max_length=1, choices=SECTOR_CHOICES)
    floors = models.PositiveIntegerField(validators=[MinValueValidator(2), MaxValueValidator(7)])

    def __str__(self) -> str:
        return "Building " + str(self.BuildingNo)


class Flat(models.Model):

    FlatNo = models.CharField(max_length=2)
    BuildingNo = models.ForeignKey(Building, on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    resident = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.FlatNo)
