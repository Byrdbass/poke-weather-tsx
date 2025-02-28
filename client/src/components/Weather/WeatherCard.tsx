import React from "react";
import { useWeather } from "../../providers/WeatherProvider";
import './weatherCard.css'


const WeatherCard: React.FC = () => {
    const {
        tempF,
        cityName,
        description,
        iconURL,
        windSpeed
    } = useWeather()
    return (
        <div>
            <div className="weather-inner-div">
                <p className="city-name">{cityName}</p>
                <p className="tempF">{tempF}</p>
                <p className="description">{description}</p>
                <p className="wind-speed">{windSpeed}</p>
                <div className="weather-icon-div">
                    <img src={iconURL} alt="" />
                </div>
            </div>
        </div>
    )
}


export default WeatherCard