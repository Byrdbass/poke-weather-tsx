import requests
import pandas as pd

def fetch_weather(city):
    # avoiding import loop - define var here inside function
    from weather_scraper.config import API_KEY, BASE_URL
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
            "feels_like": data['main']['feels_like'],
            "temp_min": data["main"]['temp_min'],
            "temp_max": data['main']['temp_max'],
            "pressure" : data['main']['pressure'],
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
