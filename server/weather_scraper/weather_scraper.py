import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# create database url and start database engine

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png",
            "timestamp": pd.Timestamp.now()
        }
        print(weather_data)
        return weather_data
    else:
        print(f"Failed to fetch data for {city}: {response.status_code}")
        return None
fetch_weather("Miami")