from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
import time
from weather_scraper.store_weather import store_weather_data
from db.weather_scraper_db.create_weather_table import create_weather_table
from db.poke_weather_match_db.create_poke_weather_match import create_poke_weather_match

# def update_weather_table():
#     with engine.connect() as conn:
#         conn.execute(text("""
#             ALTER TABLE weather
#             ADD COLUMN feels_like FLOAT,
#             ADD COLUMN temp_min FLOAT,
#             ADD COLUMN temp_max FLOAT,
#             ADD COLUMN pressure INT;
#         """))
#     print("Weather table UPDATED with new columns!")

# scheduler = BackgroundScheduler()
# scheduler.add_job(store_weather_data, "interval", minutes=1)  
# scheduler.start()


if __name__ == "__main__":
    # create_weather_table()
    create_poke_weather_match()
    print("Starting weather data collection...")
    store_weather_data()
    # while True:
    #     time.sleep(16)