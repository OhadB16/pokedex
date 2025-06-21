import db
from .state import captured_pokemon
from .utils import generate_uuid_from_number, format_pokemon, deduplicate_by_key

def fetch_raw_data():
    """Fetch fresh data from DB and attach unique IDs."""
    pokemons_raw_data = db.get()
    number_to_id = {}
    enriched_pokemons_data = []

    for pokemon_raw_data in pokemons_raw_data:
        number = pokemon_raw_data["number"]
        if number not in number_to_id:
            number_to_id[number] = generate_uuid_from_number(number)

        enriched_pokemons_data.append({
            **pokemon_raw_data,
            "id": number_to_id[number],
        })

    return enriched_pokemons_data

def get_pokemons(page, limit, sort, type_filter):
    pokemons_data = fetch_raw_data()

    if type_filter:
        pokemons_data = [
            pokemon_data for pokemon_data in pokemons_data if type_filter.lower() in (
                pokemon_data.get("type_one", "").lower(),
                pokemon_data.get("type_two", "").lower()
            )
        ]

    pokemons_data = deduplicate_by_key(pokemons_data, key="number")

    reverse = (sort == "desc")
    pokemons_data.sort(key=lambda p: p["number"], reverse=reverse)

    start = (page - 1) * limit
    end = start + limit
    paginated_pokemons_data = pokemons_data[start:end]

    return [format_pokemon(p) for p in paginated_pokemons_data]

def toggle_capture(name):
    if name in captured_pokemon:
        captured_pokemon.remove(name)
    else:
        captured_pokemon.add(name)


def get_captured():
    return list(captured_pokemon)
