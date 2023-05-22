from django.db import models
import googlemaps
from django.http import HttpResponse
from django.db.models import JSONField


class Route(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    route_points = models.JSONField(default=list)


class Location(models.Model):
    gpsPoint = models.CharField(max_length=100)



