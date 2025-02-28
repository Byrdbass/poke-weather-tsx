import { PokemonSprites, PokemonAbility, PokemonType, PokemonStat } from "pokenode-ts";

export default interface PokemonData {
    id: number;
    name: string;
    sprites: {
        back_default: string;
        back_female: string;
        back_shiny: string
        back_shiny_female: string;
        front_default: string;
        front_female: string;
        front_shiny: string;
        front_shiny_female: string;
    };
    cries: {
        latest: string;
        legacy: string;
    }
    types: PokemonType[];
    stats: PokemonStat[];
}