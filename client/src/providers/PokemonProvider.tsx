import React, { createContext, useState, useEffect, ReactNode, useContext, useRef } from "react";

import { getPokemonDataByName } from "../api/fetchPokemon";
import { PokemonData } from "../../types/index.ts";

interface PokemonContextType {
    pokeID: number;
    setPokeId: (id: number) => void;
    pokemonName: string;
    setPokemonName: (pokemonName: string) => void;
    spriteFrontDefault: string;
    setSpriteFrontDefault: (spriteFrontDefault: string) => void;
}

const PokemonContext = createContext<PokemonContextType>({
    pokeID: 0,
    setPokeId: () => {},
    pokemonName: "",
    setPokemonName: () => {},
    spriteFrontDefault: "",
    setSpriteFrontDefault: () => {}

});

interface PokemonProviderProps {
    children: ReactNode;
};

const PokemonProvider: React.FC<PokemonProviderProps> = ({ children }) => {
    const isFirstRender = useRef(true);

    const [pokeID, setPokeId] = useState<number>(0);
    const [pokemonName, setPokemonName] = useState<string>("pikachu");
    const [spriteFrontDefault, setSpriteFrontDefault] = useState<string>("")

    useEffect(()=>{
        if(isFirstRender.current){
            isFirstRender.current = false;
            return
        }
        getPokemonDataByName(pokemonName)
        .then((data: PokemonData) => {
            console.log(data)
            setPokeId(data.id);
            setSpriteFrontDefault(data.sprites.front_default)
            // setPokemonName(data.pokemonName);

        })
        .catch((e) => {
            console.error("error fetching pokemon data: ", e)
        })
    },[pokemonName])

    const value: PokemonContextType = {
        pokeID,
        setPokeId,
        pokemonName,
        setPokemonName,
        spriteFrontDefault,
        setSpriteFrontDefault
    }

    return (
        <PokemonContext.Provider value={value}>
            {children}
        </PokemonContext.Provider>
    )
}

const usePokemon = () => {
    const context = useContext(PokemonContext);
    if(!context) {
        throw new Error("usePokemon  must be used within a PokemonProvider")
    }
    return context;
}

export { PokemonProvider, usePokemon }
