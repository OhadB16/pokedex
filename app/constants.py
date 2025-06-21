# Route paths
GET_POKEMON_LIST = "/api/pokemon"
GET_CAPTURED = "/api/captured"
POST_CAPTURE = "/api/capture/<string:name>"
GET_ICON = "/api/icon/<name>"

# Query param keys
QUERY_PAGE = "page"
QUERY_LIMIT = "limit"
QUERY_SORT = "sort"
QUERY_TYPE = "type"

# Default query param values
DEFAULT_PAGE = 1
DEFAULT_LIMIT = 10
DEFAULT_SORT = "asc"

# Image URLs
POKEMON_ICON_URL = "https://img.pokemondb.net/sprites/silver/normal/{name}.png"
POKEMON_IMAGE_URL_HIGH_RES = "https://img.pokemondb.net/artwork/{name}.jpg"
POKEMON_IMAGE_URL_LOW_RES = "https://img.pokemondb.net/sprites/silver/normal/{name}.png"

# Field keys
FIELD_ERROR = "error"
FIELD_CAPTURED = "captured"

# HTTP methods
HTTP_GET = "GET"
HTTP_POST = "POST"

# Error messages
ERROR_FETCH_POKEMON_LIST = "Failed to fetch Pokémon list"
ERROR_FETCH_CAPTURED = "Failed to fetch captured Pokémon"
ERROR_CAPTURE = "Failed to capture Pokémon '{}'"
ERROR_GET_ICON = "Failed to get Pokémon icon for '{}'"
GENERIC_500_ERROR_CODE = 500
