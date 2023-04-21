from django.db import models
from PoolMate.UserSection.models import CustomUser

class Route(models.Model):
    driverId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    passengerId = models.ManyToManyField(CustomUser, related_name='rides_taken')
