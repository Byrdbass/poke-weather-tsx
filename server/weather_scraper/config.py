import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from config.connection import HOST, USER, DB_PASSWORD, DB_NAME

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

DB_URL = f"mysql+pymysql://{USER}:{DB_PASSWORD}@{HOST}/{DB_NAME}"
engine = create_engine(DB_URL)

EXTREME_CITIES = ["Denver", "Agata", "Rhyolite", "Oymyakon", "Las Vegas", "Honolulu", "Loma", "Wellington"]
# "Loma Montana"
CITIES = [
    "New York", "Los Angeles", "Chicago", "Miami", "Seattle", "Toronto", "Mexico City", "São Paulo", "Buenos Aires", 
    "London", "Paris", "Berlin", "Madrid", "Rome", "Amsterdam", "Copenhagen", "Stockholm", "Oslo", "Helsinki", "Dublin",
    "Moscow", "Istanbul", "Dubai", "Mumbai", "Delhi", "Beijing", "Shanghai", "Tokyo", "Seoul", "Bangkok",
    "Jakarta", "Singapore", "Kuala Lumpur", "Manila", "Sydney", "Melbourne", "Auckland", "Cape Town", "Johannesburg", "Cairo",
    "Lagos", "Nairobi", "Casablanca", "Doha", "Riyadh", "Tehran", "Baghdad", "Karachi", "Dhaka", "Hanoi",
    "Ho Chi Minh City", "Taipei", "Hong Kong", "Macau", "Vancouver", "San Francisco", "Houston", "Dallas", "Washington D.C.", "Boston"
]