import polyline as polyline
import requests
from gmplot import gmplot

# Define the API endpoint for the Directions API
endpoint = "https://maps.googleapis.com/maps/api/directions/json"

# Define the API parameters
params = {
"origin": "Universidad EAFIT, Medellin, Colombia",
"destination": "Calle 21#81-70, Medellin, Colombia",
"key": "AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg" # Replace with your own API key
}

# Send the API request
response = requests.get(endpoint, params=params).json()
# Extract the encoded polyline from the response
encoded_polyline = response["routes"][0]["overview_polyline"]["points"]

# Decode the polyline into a list of coordinates
route_points = polyline.decode(encoded_polyline)

# Create the plot object
gmap = gmplot.GoogleMapPlotter(0, 0, 2)

for lats, lngs in route_points:
    gmap.marker(lats,lngs)

# Plot the route on the map
lats, lngs = zip(*route_points)
print(route_points)
gmap.plot(lats, lngs, 'cornflowerblue', edge_width=10)

# Save the map to an HTML file
gmap.draw("route.html")
