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

HOST = os.getenv("DB_HOST_NAME")
USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DB_URL = f"mysql+pymysql://{USER}:{DB_PASSWORD}@127.0.0.1:3306/{DB_NAME}"
engine = create_engine(DB_URL)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_all_pokemon():
    response = requests.get(f"{POKEAPI_BASE_URL}?limit=2000")
    
    if response.status_code == 200:
        data = response.json()
        pokemon_list = data.get("results", [])
        return pokemon_list
    else:
        print(f"Error fetching Pokémon list: {response.status_code}")
        return []
    
def fetch_pokemon_details(pokemon_url):

    response = requests.get(pokemon_url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "name": data["name"],
            # MAY NOT BE NEEDED UNLESS BATTLE DESIGN IMPLEMENTED
            # "height": data["height"],
            # "weight": data["weight"],
            # "base_experience": data["base_experience"],
            # "hp": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "hp"),
            # "attack": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "attack"),
            # "defense": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "defense"),
            # "speed": next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "speed"),
            "sprite_front": data["sprites"]["front_default"],
            "sprite_female_front": data["sprites"]["front_female"] if "front_female" in data['sprites'] else None,
            "sprite_back": data["sprites"]["back_default"],
            "sprite_shiny": data["sprites"]["front_shiny"],
            "cry": data["cries"]["latest"] if "cries" in data and "latest" in data["cries"] else None,
            "types": ", ".join(t["type"]["name"] for t in data["types"]),
        }
    else:
        print(f"Failed to fetch data for {pokemon_url}")
        return None
    
def store_pokemon_data():
    pokemon_list = fetch_all_pokemon()
    
    if not pokemon_list:
        print("No Pokémon data retrieved.")
        return

    pokemon_records = []
    
    for pokemon in pokemon_list:
        details = fetch_pokemon_details(pokemon["url"])
        if details:
            pokemon_records.append(details)
        # time.sleep(1)  # Prevents hitting API rate limits

    if pokemon_records:
        df = pd.DataFrame(pokemon_records)
        df.to_sql("pokemon", con=engine, if_exists="append", index=False)
        print(f"Stored {len(pokemon_records)} Pokémon records at {pd.Timestamp.now()}")
        
def create_pokemon_table():
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            sprite_front VARCHAR(255),
            sprite_female_front VARCHAR(255),
            sprite_back VARCHAR(255),
            sprite_shiny VARCHAR(255),
            cry VARCHAR(255),
            types VARCHAR(255)
        );
        """))
    print("Pokemon table CREATED!")

if __name__ == "__main__":
    create_pokemon_table()
    print("Starting Pokémon data collection...")
    store_pokemon_data()