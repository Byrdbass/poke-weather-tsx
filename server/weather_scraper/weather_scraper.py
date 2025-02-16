import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

HOST = os.getenv("DB_HOST_NAME")
USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DB_URL = f"mysql+pymysql://{USER}:{DB_PASSWORD}@127.0.0.1:3306/{DB_NAME}"
engine = create_engine(DB_URL)

CITIES = [
    "New York", "Los Angeles", "Chicago", "Miami", "Seattle", "Toronto", "Mexico City", "São Paulo", "Buenos Aires", 
    "London", "Paris", "Berlin", "Madrid", "Rome", "Amsterdam", "Copenhagen", "Stockholm", "Oslo", "Helsinki", "Dublin",
    "Moscow", "Istanbul", "Dubai", "Mumbai", "Delhi", "Beijing", "Shanghai", "Tokyo", "Seoul", "Bangkok",
    "Jakarta", "Singapore", "Kuala Lumpur", "Manila", "Sydney", "Melbourne", "Auckland", "Cape Town", "Johannesburg", "Cairo",
    "Lagos", "Nairobi", "Casablanca", "Doha", "Riyadh", "Tehran", "Baghdad", "Karachi", "Dhaka", "Hanoi",
    "Ho Chi Minh City", "Taipei", "Hong Kong", "Macau", "Vancouver", "San Francisco", "Houston", "Dallas", "Washington D.C.", "Boston"
]


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

def store_weather_data():
    weather_records = [fetch_weather(city) for city in CITIES]
    weather_records = [record for record in weather_records if record]  # Filter out failed requests

    if weather_records:
        df = pd.DataFrame(weather_records)
        df.to_sql("weather", con=engine, if_exists="append", index=False)
        print(f"Stored {len(weather_records)} records at {pd.Timestamp.now()}")

def create_weather_table():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS weather (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(255),
                temperature FLOAT,
                humidity INT,
                wind_speed FLOAT,
                description VARCHAR(255),
                icon VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """))
    print("Weather table CREATED!")

# scheduler = BackgroundScheduler()
# scheduler.add_job(store_weather_data, "interval", minutes=1)  
# scheduler.start()


if __name__ == "__main__":
    create_weather_table()
    store_weather_data()
    print("Starting weather data collection...")
    while True:
        time.sleep(16)