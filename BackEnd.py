import googlemaps
import gmaps

# Replace YOUR_API_KEY with your actual API key
gmaps.configure(api_key='AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg')

# Get your location
gmaps_location = gmaps.datasets.load_dataset('taxi_rides')
lat, lng = gmaps_location[0][0]

# Create a map centered on your location
fig = gmaps.figure(center=(lat, lng), zoom_level=13)

# Add a marker for your location
marker_locations = [(lat, lng)]
markers = gmaps.marker_layer(marker_locations)
fig.add_layer(markers)

# Display the map
fig
