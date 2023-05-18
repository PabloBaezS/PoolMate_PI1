from django.db import models
from UserSection.models import User
import googlemaps
from django.http import HttpResponse


class Route(models.Model):
    driverId = models.ForeignKey(User, on_delete=models.CASCADE)
    passengerId = models.ManyToManyField(User, related_name='rides_taken')
    routeId = models.IntegerField()
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)



    def save_route(request):
        # retrieve route data from Google Maps API
        gmaps = googlemaps.Client(key='YOUR_API_KEY')
        directions_result = gmaps.directions(origin='San Francisco',
                                             destination='Los Angeles',
                                             mode='driving',
                                             waypoints=[('Bakersfield', 'via:CA-99')],
                                             optimize_waypoints=True)

        # extract relevant information from route data
        start_latitude = directions_result[0]['legs'][0]['start_location']['lat']
        start_longitude = directions_result[0]['legs'][0]['start_location']['lng']
        end_latitude = directions_result[0]['legs'][0]['end_location']['lat']
        end_longitude = directions_result[0]['legs'][0]['end_location']['lng']
        distance = directions_result[0]['legs'][0]['distance']['value']
        duration = directions_result[0]['legs'][0]['duration']['value']
        waypoints = [(waypoint['location']['lat'], waypoint['location']['lng']) for waypoint in directions_result[0]['waypoint_order']]

        # create and save Route instance
        route = Route(start_latitude=start_latitude,
                      start_longitude=start_longitude,
                      end_latitude=end_latitude,
                      end_longitude=end_longitude,
                      distance=distance,
                      duration=duration,
                      waypoints=waypoints)
        route.save()

        return HttpResponse('Route saved successfully!')


class Location(models.Model):
    gpsPoint = models.CharField(max_length=100)

#def main():
    # print(Route.save_route())

#main()

