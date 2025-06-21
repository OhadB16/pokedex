from flask import request, jsonify
from .services import get_pokemons, toggle_capture, get_captured
from .state import captured_pokemon
from .constants import (
    GET_POKEMON_LIST,
    GET_CAPTURED,
    POST_CAPTURE,
    GET_ICON,
    POKEMON_ICON_URL,
    DEFAULT_PAGE,
    DEFAULT_LIMIT,
    DEFAULT_SORT,
    QUERY_PAGE,
    QUERY_LIMIT,
    QUERY_SORT,
    QUERY_TYPE,
    FIELD_ERROR,
    FIELD_CAPTURED,
    HTTP_GET,
    HTTP_POST,
    ERROR_FETCH_POKEMON_LIST,
    ERROR_FETCH_CAPTURED,
    ERROR_CAPTURE,
    ERROR_GET_ICON,
    GENERIC_500_ERROR_CODE,
)
import logging

logger = logging.getLogger(__name__)

def register_routes(app):
    @app.route(GET_POKEMON_LIST)
    def get_pokemon_list():
        try:
            args = request.args
            page = int(args.get(QUERY_PAGE, DEFAULT_PAGE))
            limit = int(args.get(QUERY_LIMIT, DEFAULT_LIMIT))
            sort = args.get(QUERY_SORT, DEFAULT_SORT)
            type_filter = args.get(QUERY_TYPE)
            return jsonify(get_pokemons(page, limit, sort, type_filter))
        except Exception as e:
            logger.exception(f"{ERROR_FETCH_POKEMON_LIST}: {e}")
            return jsonify({FIELD_ERROR: ERROR_FETCH_POKEMON_LIST}), GENERIC_500_ERROR_CODE

    @app.route(GET_CAPTURED, methods=[HTTP_GET])
    def list_captured():
        try:
            return jsonify(get_captured())
        except Exception as e:
            logger.exception(f"{ERROR_FETCH_CAPTURED}: {e}")
            return jsonify({FIELD_ERROR: ERROR_FETCH_CAPTURED}), GENERIC_500_ERROR_CODE

    @app.route(POST_CAPTURE, methods=[HTTP_POST])
    def capture(name):
        try:
            toggle_capture(name)
            return jsonify({FIELD_CAPTURED: name in captured_pokemon})
        except Exception as e:
            logger.exception(ERROR_CAPTURE.format(name, e))
            return jsonify({FIELD_ERROR: ERROR_CAPTURE.format(name)}), GENERIC_500_ERROR_CODE

    @app.route(GET_ICON)
    def icon(name):
        try:
            return POKEMON_ICON_URL.format(name=name.lower())
        except Exception as e:
            logger.exception(ERROR_GET_ICON.format(name, e))
            return jsonify({FIELD_ERROR: ERROR_GET_ICON.format(name)}), GENERIC_500_ERROR_CODE
