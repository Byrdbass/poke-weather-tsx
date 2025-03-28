import { useState } from "react";
import { WeatherProvider } from "./providers/WeatherProvider";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import './assets/fonts/PokemonGb-RAeo.ttf';
import WeatherCard from "./components/Weather/WeatherCard";
import { PokemonProvider } from "./providers/PokemonProvider";
import PokeCard from "./components/Pokemon/PokeCard";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <WeatherProvider>
        <PokemonProvider>
          <PokeCard />
           <WeatherCard />
        <div>
          <a href="https://vite.dev" target="_blank">
            <img src={viteLogo} className="logo" alt="Vite logo" />
          </a>
          <a href="https://react.dev" target="_blank">
            <img src={reactLogo} className="logo react" alt="React logo" />
          </a>
        </div>
        <h1>Vite + React</h1>
        <div className="card">
          <button onClick={() => setCount((count) => count + 1)}>
            count is {count}
          </button>
          <p>
            Edit <code>src/App.tsx</code> and save to test HMR
          </p>
        </div>
        <p className="read-the-docs">
          Click on the Vite and React logos to learn more
        </p>
        </PokemonProvider>
      </WeatherProvider>
    </>
  );
}

export default App;
