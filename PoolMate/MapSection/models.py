from django.db import models
from UserSection.models import User

class Route(models.Model):
    driverId = models.ForeignKey(User, on_delete=models.CASCADE)
    passengerId = models.ManyToManyField(User, related_name='rides_taken')
    routeId = models.IntegerField()
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)

class Location(models.Model):
    gpsPoint = models.CharField(max_length=100)


