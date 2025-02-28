import { PokemonClient } from "pokenode-ts";
import { PokemonData } from "../../types/index.ts";

const getPokemonDataByName = async (pokemonName: string): Promise<PokemonData> => {
    const api = new PokemonClient();
    if(!api) throw new Error("failed to connect to API")
    const data = await api.getPokemonByName(pokemonName);
    //TODO create function to get pokemondata by id
    console.log(data)
    return data;
}

export { getPokemonDataByName };