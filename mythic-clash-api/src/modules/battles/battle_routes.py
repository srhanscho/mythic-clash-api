from flask import Blueprint, request, jsonify
from modules.battles import battle_service as service
from utils.helpers import error_response


battles_bp = Blueprint("battles", __name__, url_prefix="/battle")


@battles_bp.route("", methods=["POST"])
def battle():
    """Ejecuta una batalla entre dos personajes."""
    data = request.get_json(silent=True)

    if data is None:
        return error_response("Request body must be valid JSON.", 400)

    response, status_code = service.run_battle(data)
    return jsonify(response), status_code