from django.shortcuts import render, redirect
from .models import Route
import os
import polyline
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from gmplot import gmplot
from UserSection.models import Passenger

def route(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Define the API endpoint for the Directions API
        endpoint = "https://maps.googleapis.com/maps/api/directions/json"

        # Set your Google Maps API key
        key = "AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg"

        # Define the API parameters
        params = {
            "origin": origin,
            "destination": destination,
            "key": key
        }

        # Send the API request
        response = requests.get(endpoint, params=params).json()

        # Check if routes are available in the response
        if "routes" in response and len(response["routes"]) > 0:
            # Extract the encoded polyline from the first route
            encoded_polyline = response["routes"][0]["overview_polyline"]["points"]

            # Decode the polyline into a list of coordinates
            route_points = polyline.decode(encoded_polyline)

            # Create the plot object
            gmap = gmplot.GoogleMapPlotter.from_geocode("Medellin, Colombia")

            # Plot the route on the map
            lats, lngs = zip(*route_points)
            gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)

            # Save the map to a temporary file
            temp_folder = os.path.join(settings.BASE_DIR, 'temp')
            os.makedirs(temp_folder, exist_ok=True)  # Create the "temp" folder if it doesn't exist
            map_file_path = os.path.join(temp_folder, 'map.html')
            gmap.draw(map_file_path)

            # Get the relative URL for the map file
            map_file_url = os.path.join('temp', 'map.html')

            return JsonResponse({'success': True, 'redirect_url': map_file_url})

        return JsonResponse({'success': False, 'error': 'No route found'})

    return render(request, 'route.html')




def driver_view(request):
    return render(request, 'driverView.html')

def passenger_view(request):
    if request.method == 'POST':
        location = request.POST.get('location')

        # Here you can process and save the location as needed
        # For example, you can save it to a database or perform other operations

        # Render a success page or redirect to another view
        return render(request, 'success.html')

    # Render the form page if it's a GET request
    return render(request, 'passengerView.html')


def save_route(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Perform the necessary operations to get the route points and save the route
        # For example, you can use the code from the previous response to save the route points

        route = Route.objects.create(origin=origin, destination=destination, route_points=route_points)
        return redirect('driver_view')




def save_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        passenger = Passenger.objects.get(id=request.user.id)
        passenger.location = location
        passenger.save()

    return redirect('passenger_view')

