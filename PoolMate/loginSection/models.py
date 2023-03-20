from django.db import models

class UserProfile(models.Model):
    id = models.IntegerField(max_length=5)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.EmailField(max_length=15)
    homeAddress = models.CharField(max_length=100)

# Create your models here.
