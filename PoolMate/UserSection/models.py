from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9._%+-]+@eafit\.edu\.co$', 'Enter a valid eafit.edu.co email address.')])
    phone = models.CharField(max_length=20)
    homeAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    licensePlate = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    driverId = models.CharField(max_length=50)
    capacity = models.IntegerField()


class Driver(CustomUser):
    driverLicense = models.CharField(max_length=50)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rate = models.FloatField()
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True, primary_key=True)


class Passenger(CustomUser):
    pickup = models.CharField(max_length=200)
    dropoff = models.CharField(max_length=200)
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True, primary_key=True)


class Admin(CustomUser):
    account = models.CharField(max_length=100)
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE, parent_link=True, primary_key=True)
