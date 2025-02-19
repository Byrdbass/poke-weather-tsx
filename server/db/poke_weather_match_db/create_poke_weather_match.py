from weather_scraper.config import engine
from sqlalchemy.sql import text;

def create_poke_weather_match():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS pokemon_weather_match (
                id INT AUTO_INCREMENT PRIMARY KEY,
                pokemon_id INT,
                pokemon_name VARCHAR(255),
                pokemon_type VARCHAR(255),
                temperature FLOAT,
                humidity INT,
                wind_speed FLOAT,
                pressure INT,
                weather_description VARCHAR(255),
                weather_icon VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
            );
        """))
    print("Poke_weather_match table CREATED")