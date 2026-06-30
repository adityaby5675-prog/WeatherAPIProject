import requests

city = input("Enter city name: ")

# Step 1: Get latitude and longitude
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)

geo_data = geo_response.json()

if "results" not in geo_data:
    print("City not found!")
    exit()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

# Step 2: Get weather data
weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,wind_speed_10m"
)

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

print("\n------ Weather Report ------")
print("City:", city.title())
print("Temperature:", weather_data["current"]["temperature_2m"], "°C")
print("Wind Speed:", weather_data["current"]["wind_speed_10m"], "km/h")