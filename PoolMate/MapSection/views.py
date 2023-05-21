from django.shortcuts import render, redirect
from .forms import CreateRideForm
import polyline as polyline
import requests
from gmplot import gmplot
from .models import Route


def route(request):
    # Define the API endpoint for the Directions API
    endpoint = "https://maps.googleapis.com/maps/api/directions/json"

    origin = 'Universidad EAFIT, Medellin, Colombia'
    destination = 'Calle 21#81-70, Medellin, Colombia'
    key = 'AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg'

    # Define the API parameters
    params = {
        "origin": origin,
        "destination": destination,
        "key": key
    }

    # Send the API request
    response = requests.get(endpoint, params=params).json()
    # Extract the encoded polyline from the response
    encoded_polyline = response["routes"][0]["overview_polyline"]["points"]

    # Decode the polyline into a list of coordinates
    route_points = polyline.decode(encoded_polyline)

    # Save the route data to the database
    route = Route.objects.create(origin=origin, destination=destination, route_points=route_points)

    # Create the plot object
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)

    for lat, lng in route_points:
        gmap.marker(lat, lng)

    # Plot the route on the map
    lats, lngs = zip(*route_points)
    gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)

    # Save the map to an HTML file
    gmap.draw("route.html")

    # Render the HTML page
    return render(request, 'route.html')


def driver_view(request):
    return render(request, 'driverView.html')


def save_route(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Perform the necessary operations to get the route points and save the route
        # For example, you can use the code from the previous response to save the route points

        route = Route.objects.create(origin=origin, destination=destination, route_points=route_points)
        return redirect('driver_view')
