from django.core.validators import RegexValidator
from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9._%+-]+@eafit\.edu\.co$', 'Enter a valid eafit.edu.co email address.')])
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    homeAddress = models.CharField(max_length=200)

class Driver(User):
    driverLicense = models.CharField(max_length=50)
    car = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    rate = models.FloatField()

class Passenger(User):
    pickup = models.CharField(max_length=200)
    dropoff = models.CharField(max_length=200)

class Admin(User):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)

class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    licensePlate = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    driverId = models.CharField(max_length=50)
    capacity = models.IntegerField()
