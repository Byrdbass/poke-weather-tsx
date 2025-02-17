import pandas as pd
from weather_scraper import engine, EXTREME_CITIES, CITIES
import weather_scraper.fetch_weather


def store_weather_data():
    # avoiding import loop - define var here inside function
    fetch_weather = weather_scraper.fetch_weather
    weather_records = [fetch_weather(city) for city in EXTREME_CITIES]
    weather_records = [record for record in weather_records if record]  # Filter out failed requests

    if weather_records:
        df = pd.DataFrame(weather_records)
        df.to_sql("weather", con=engine, if_exists="append", index=False)
        print(f"Stored {len(weather_records)} records at {pd.Timestamp.now()}")
