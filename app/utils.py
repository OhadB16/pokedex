from typing import List, Dict
import uuid
import hashlib
from urllib.parse import quote
from .state import captured_pokemon

def generate_uuid_from_number(number: int) -> str:
    return str(uuid.UUID(hashlib.md5(str(number).encode()).hexdigest()))


def get_pokemon_image_url(name: str, high_res: bool = True) -> str:
    encoded_name = quote(name.lower())
    if high_res:
        return f"https://img.pokemondb.net/artwork/{encoded_name}.jpg"
    return f"https://img.pokemondb.net/sprites/silver/normal/{encoded_name}.png"


def deduplicate_by_key(data: List[Dict], key: str) -> List[Dict]:
    seen = set()
    result = []
    for item in data:
        value = item.get(key)
        if value not in seen:
            seen.add(value)
            result.append(item)
    return result

def format_pokemon(pokemon_data):
    name = pokemon_data["name"].lower()
    image_url = get_pokemon_image_url(name, high_res=True)

    return {
        "id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "number": pokemon_data["number"],
        "type": list(filter(None, [
            pokemon_data.get("type_one"),
            pokemon_data.get("type_two")
        ])),
        "image_url": image_url,
        "hp": pokemon_data.get("hit_points"),
        "atk": pokemon_data.get("attack"),
        "def": pokemon_data.get("defense"),
        "spd": pokemon_data.get("speed"),
        "captured": pokemon_data["name"] in captured_pokemon,
    }