#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

import requests

API_KEY = "YOUR API KEY HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat="
GEO_BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?q="

#get geo long and lat

city_name = input("enter a city name: ")
geo_request_url = f"{GEO_BASE_URL}{city_name}&limit=5&appid={API_KEY}"
geo_response = requests.get(geo_request_url)
geo_data = geo_response.json()
lat = geo_data[0]["lat"]
long = geo_data[0]["lon"]


request_url = f"{BASE_URL}{lat}&lon={long}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("error:" + response)
