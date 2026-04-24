from modules.characters import character_repository as repo


# Campos numéricos sujetos a validación.
STAT_FIELDS = ["strength", "agility", "magic", "knowledge"]

# Rango permitido para estadísticas de combate.
STAT_MIN = 0
STAT_MAX = 100


def _validate_stats(data):
    """Valida que las estadísticas existan y estén dentro del rango permitido."""
    errors = []

    for field in STAT_FIELDS:
        value = data.get(field)

        if value is None:
            errors.append(f"Field '{field}' is required.")
            continue

        if not isinstance(value, int):
            errors.append(f"Field '{field}' must be an integer.")
            continue

        if value < STAT_MIN or value > STAT_MAX:
            errors.append(
                f"Field '{field}' must be between {STAT_MIN} and {STAT_MAX}. Received: {value}."
            )

    return errors


def _validate_text_fields(data):
    """Valida que los campos de texto requeridos estén presentes."""
    errors = []
    text_fields = ["name", "skin_color", "race"]

    for field in text_fields:
        value = data.get(field)

        if not value or not isinstance(value, str) or value.strip() == "":
            errors.append(f"Field '{field}' is required and must be a valid text.")

    return errors


def get_all_characters():
    """Retorna el listado completo de personajes."""
    characters = repo.find_all()

    return {
        "success": True,
        "message": "Characters retrieved successfully.",
        "data": {
            "characters": characters,
            "total": len(characters)
        }
    }, 200


def get_character_by_id(character_id):
    """Retorna un personaje por identificador."""
    character = repo.find_by_id(character_id)

    if not character:
        return {
            "success": False,
            "message": f"Character with id={character_id} was not found."
        }, 404

    return {
        "success": True,
        "message": "Character retrieved successfully.",
        "data": {
            "character": character
        }
    }, 200


def create_character(data):
    """Crea un personaje a partir de los datos recibidos."""
    text_errors = _validate_text_fields(data)
    if text_errors:
        return {
            "success": False,
            "message": "Invalid character data.",
            "details": text_errors
        }, 400

    stat_errors = _validate_stats(data)
    if stat_errors:
        return {
            "success": False,
            "message": "Invalid character stats.",
            "details": stat_errors
        }, 400

    name = data["name"].strip()
    existing = repo.find_by_name(name)

    if existing:
        return {
            "success": False,
            "message": f"A character with the name '{name}' already exists."
        }, 409

    new_id = repo.insert(
        name=name,
        skin_color=data["skin_color"].strip(),
        race=data["race"].strip(),
        strength=data["strength"],
        agility=data["agility"],
        magic=data["magic"],
        knowledge=data["knowledge"],
    )

    created = repo.find_by_id(new_id)

    return {
        "success": True,
        "message": "Character created successfully.",
        "data": {
            "character": created
        }
    }, 201


def update_character(character_id, data):
    """Actualiza los datos de un personaje existente."""
    existing = repo.find_by_id(character_id)

    if not existing:
        return {
            "success": False,
            "message": f"Character with id={character_id} was not found."
        }, 404

    text_errors = _validate_text_fields(data)
    stat_errors = _validate_stats(data)
    errors = text_errors + stat_errors

    if errors:
        return {
            "success": False,
            "message": "Invalid character data.",
            "details": errors
        }, 400

    new_name = data["name"].strip()

    if new_name.lower() != existing["name"].lower():
        name_taken = repo.find_by_name(new_name)

        if name_taken:
            return {
                "success": False,
                "message": f"A character with the name '{new_name}' already exists."
            }, 409

    repo.update(
        character_id=character_id,
        name=new_name,
        skin_color=data["skin_color"].strip(),
        race=data["race"].strip(),
        strength=data["strength"],
        agility=data["agility"],
        magic=data["magic"],
        knowledge=data["knowledge"],
    )

    updated = repo.find_by_id(character_id)

    return {
        "success": True,
        "message": "Character updated successfully.",
        "data": {
            "character": updated
        }
    }, 200


def delete_character(character_id):
    """Elimina un personaje registrado."""
    existing = repo.find_by_id(character_id)

    if not existing:
        return {
            "success": False,
            "message": f"Character with id={character_id} was not found."
        }, 404

    repo.delete(character_id)

    return {
        "success": True,
        "message": f"Character '{existing['name']}' deleted successfully.",
        "data": None
    }, 200