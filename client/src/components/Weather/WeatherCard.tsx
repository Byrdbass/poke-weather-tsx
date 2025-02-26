import React from "react";
import { useWeather } from "../../providers/WeatherProvider";
import './weatherCard.css'

interface Props {
    title: string;
}
const WeatherCard: React.FC<Props> = ({ title }) => {
    const {
        tempF,
        cityName,
        description,
        iconURL,
        windSpeed
    } = useWeather()
    return (
        <div>
            {title}
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