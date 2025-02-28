import React from "react";
import { usePokemon } from "../../providers/PokemonProvider";
import './pokeCard.css'

const PokeCard: React.FC = () => {
    const {
        pokeID,
        pokemonName,
        spriteFrontDefault
    } = usePokemon()

    return (
        <div>
            <p className="poke-name">{pokemonName}</p>
            <p className="poke-id-num">ID: {pokeID}</p>
            <div className="poke-img">
                {/* create dynamic alt image tag */}
                <img src={spriteFrontDefault} alt={"pic of "+ {pokemonName} }/>
            </div>

        </div>
    )
}

export default PokeCard;