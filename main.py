import os
import requests
from dotenv import load_dotenv

load_dotenv()

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")

condition_list = []

parameters = {
    "lat": 9.915488,
    "lon": -83.999890,
    "appid": api_key,
    "cnt": 5
}

response = requests.get(OMW_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

for i in range(0, parameters["cnt"]):
    condition = data["list"][i]["weather"][0]["id"]
    condition_list.append(condition)

for condition in condition_list:
    if condition < 700:
        print("Hoy hay que llevar sombrilla.")



