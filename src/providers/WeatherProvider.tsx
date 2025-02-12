import React, {createContext, useState, useEffect, ReactNode, useContext, useRef} from "react";

import { getCityWeather } from "../api/fetchWeather";
import { WeatherType } from "../../types/index.d.ts";

interface WeatherContextType {
    tempF: string;
    setTempF: (tempF: string) => void;
    cityName: string;
    setCityName: (cityName: string) => void;
    description: string;
    iconURL: string;
    windSpeed: string;
}

const WeatherContext = createContext<WeatherContextType>({
    tempF: 'N/A',
    setTempF: () => {},
    cityName: "New York",
    setCityName: () => {},
    description: "",
    iconURL: "",
    windSpeed: "",
});

interface WeatherProviderProps {
    children: ReactNode;
}

const WeatherProvider: React.FC<WeatherProviderProps> = ({ children }) => {
    const isFirstRender = useRef(true);

    const urlOneCall: string = 'https://api.openweathermap.org/data/2.5/onecall?lat=';
    
    const [tempF, setTempF] = useState<string>("N/A");
    const [cityName, setCityName] = useState<string>("New York");
    const [description, setDescription] = useState<string>("");
    const [iconURL, setIconURL] = useState<string>("");
    const [windSpeed, setWindSpeed] = useState<string>("");

    useEffect(() => {
        if(isFirstRender.current){
            isFirstRender.current = false;
            return
        }
        getCityWeather(cityName)
            .then((data: WeatherType) => {
                setTempF(`${data.main.temp}°F`);
                setDescription(data.weather[0].description);
                setIconURL(`https://openweathermap.org/img/wn/${data.weather[0].icon}.png`);
                setWindSpeed(`${data.wind.speed} mph`);
            })
            .catch((error) => {
                console.error("Error fetching weather data:", error);
            });
        // if (navigator.geolocation){
        //     navigator.geolocation.getCurrentPosition(successCallback:);
        // }

    }, [cityName])
    console.log(tempF, cityName, windSpeed)
    const value: WeatherContextType = {
        tempF,
        setTempF,
        cityName,
        setCityName,
        description,
        iconURL,
        windSpeed,
    };

    return (
        <WeatherContext.Provider value={value}>
            {children}
        </WeatherContext.Provider>
    )
}

const useWeather = () => {
    const context = useContext(WeatherContext);
    if (!context) {
        throw new Error("useWeather must be used within a WeatherProvider")
    }
    return context;
}

export { WeatherProvider, useWeather }