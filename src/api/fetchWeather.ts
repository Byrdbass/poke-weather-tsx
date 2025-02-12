import { WeatherType } from '../../types/index.ts'

const apiKey: string = import.meta.env.VITE_WEATHER_API_KEY
const urlByCity: string = 'https://api.openweathermap.org/data/2.5/weather?q='

const getCityWeather = async (cityName: string): Promise<WeatherType> => {
    const response = await fetch(`${urlByCity}${cityName}&units=imperial&appid=${apiKey}`)
    if (!response.ok) {
        throw new Error("Failed to fetch weather data");
    }
    const data: WeatherType = await response.json();
    return data;
}

export { getCityWeather }