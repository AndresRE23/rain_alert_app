import os
import requests
from dotenv import load_dotenv
import smtplib

load_dotenv()

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")
my_email = "andresre2311@gmail.com"
password = "lztaajelqrvhdkmj"

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
    if 200 <= condition_code < 600:
        will_rain = True
        break

if will_rain:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as cn:
        cn.starttls()
        cn.login(my_email, password)
        cn.sendmail(my_email, my_email, msg="Subject:️Hoy podría llover 🌧️\n\nHola,\n\nSegún el pronóstico, hoy hay probabilidad de lluvia. ☂️".encode("utf-8"))



