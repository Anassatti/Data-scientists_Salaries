# importing the requests library
import requests

# api-endpoint
URL = "http://127.0.0.1:5000/predict"


r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      % (latitude, longitude, formatted_address))