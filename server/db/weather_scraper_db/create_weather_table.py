from weather_scraper.config import engine
from sqlalchemy.sql import text

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
    