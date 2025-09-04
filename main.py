import os
import requests
from dotenv import load_dotenv

load_dotenv()

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")

parameters = {
    "lat": 9.915488,
    "lon": -83.999890,
    "appid": api_key,
    "cnt": 5
}

response = requests.get(OMW_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Hoy probablemente va a llover.")



