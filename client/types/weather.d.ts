export default interface WeatherType{
    main: {
        temp: number;
    };
    name: string; 
    weather: [
        {
            description: string; 
            icon: string;
        }
    ];
    wind: {
        speed: number; 
    };
}