import requests

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2fa08b339a68ba3d2c0181e03b503771"

parameters = {
    "lat": 9.915488,
    "lon": -83.999890,
    "appid": api_key,
    "cnt": 5
}

response = requests.get(OMW_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
print(data)



