import googlemaps

# Apik Key from GooGle Maps
gmaps = googlemaps.Client(key='AIzaSyBaJ_KORpCWjJT8tP4N7L6VSRoHPHUTXFg')

# Define the origin and destination addresses
print('Enter your origin place!')
origin = input('->')
print('Enter your destination!')
destination = input('->')

print('Loading...')

# Use the Google Maps API to get the distance and travel time between the two addresses
result = gmaps.distance_matrix(origin, destination, mode='driving')

# Print the distance and travel time
distance = result['rows'][0]['elements'][0]['distance']['text']
duration = result['rows'][0]['elements'][0]['duration']['text']
print('The distance between', origin, 'and', destination, 'is', distance)
print('The travel time between', origin, 'and', destination, 'is', duration)
