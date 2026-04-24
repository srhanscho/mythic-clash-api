from flask import Blueprint, request, jsonify
from modules.characters import character_service as service
from utils.helpers import error_response


characters_bp = Blueprint("characters", __name__, url_prefix="/characters")


@characters_bp.route("", methods=["GET"])
def get_all():
    """Consulta todos los personajes registrados."""
    response, status_code = service.get_all_characters()
    return jsonify(response), status_code


@characters_bp.route("/<int:character_id>", methods=["GET"])
def get_by_id(character_id):
    """Consulta un personaje por su identificador."""
    response, status_code = service.get_character_by_id(character_id)
    return jsonify(response), status_code


@characters_bp.route("", methods=["POST"])
def create():
    """Registra un nuevo personaje."""
    data = request.get_json(silent=True)

    if data is None:
        return error_response("Request body must be valid JSON.", 400)

    response, status_code = service.create_character(data)
    return jsonify(response), status_code


@characters_bp.route("/<int:character_id>", methods=["PUT"])
def update(character_id):
    """Actualiza los datos de un personaje existente."""
    data = request.get_json(silent=True)

    if data is None:
        return error_response("Request body must be valid JSON.", 400)

    response, status_code = service.update_character(character_id, data)
    return jsonify(response), status_code


@characters_bp.route("/<int:character_id>", methods=["DELETE"])
def delete(character_id):
    """Elimina un personaje por su identificador."""
    response, status_code = service.delete_character(character_id)
    return jsonify(response), status_code