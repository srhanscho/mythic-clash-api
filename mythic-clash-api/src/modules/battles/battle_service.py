from modules.characters import character_repository as char_repo
from modules.battles import battle_logic as logic


def run_battle(data):
    """Ejecuta el flujo de negocio para una batalla entre dos personajes."""
    id1 = data.get("character1_id")
    id2 = data.get("character2_id")

    if id1 is None or id2 is None:
        return {
            "success": False,
            "message": "Fields 'character1_id' and 'character2_id' are required.",
            "details": {
                "example": {
                    "character1_id": 1,
                    "character2_id": 2
                }
            }
        }, 400

    if not isinstance(id1, int) or not isinstance(id2, int):
        return {
            "success": False,
            "message": "Character IDs must be integers."
        }, 400

    if id1 <= 0 or id2 <= 0:
        return {
            "success": False,
            "message": "Character IDs must be positive integers."
        }, 400

    if id1 == id2:
        return {
            "success": False,
            "message": "A character cannot battle against itself.",
            "details": {
                "character_id": id1
            }
        }, 400

    character1 = char_repo.find_by_id(id1)
    character2 = char_repo.find_by_id(id2)

    missing_ids = []

    if not character1:
        missing_ids.append(id1)

    if not character2:
        missing_ids.append(id2)

    if missing_ids:
        return {
            "success": False,
            "message": "One or more characters were not found.",
            "details": {
                "not_found_ids": missing_ids
            }
        }, 404

    result = logic.resolve_battle(character1, character2)

    return {
        "success": True,
        "message": "Battle resolved successfully.",
        "data": {
            "combatants": {
                "character1": {
                    "id": character1["id"],
                    "name": character1["name"]
                },
                "character2": {
                    "id": character2["id"],
                    "name": character2["name"]
                }
            },
            "result": result
        }
    }, 200