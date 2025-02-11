import React, {createContext, useState, useEffect, ReactNode, useContext} from "react";

interface WeatherContextType {
    tempF : string;
    setTempF : (tempF: string) => void;
    // tempC : string;
    //create other setters?
    // iconURL : string;
    // windSpeed: string;
    // lat: number;
    // lon: number;
}

const WeatherContext = createContext<WeatherContextType | null>(null);

interface WeatherProviderProps {
    children: ReactNode;
}

const WeatherProvider: React.FC<WeatherProviderProps> = ({ children }) => {
    const [tempF, setTempF] = useState<string>("N/A");

    const value: WeatherContextType = {
        tempF,
        setTempF
    }

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