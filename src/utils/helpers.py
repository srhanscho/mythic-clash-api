from flask import jsonify


def clamp(value, min_val, max_val):
    """
    Asegura que un valor numérico esté dentro de un rango.
    Útil para garantizar que stats no salgan del rango válido.

    Ejemplo:
        clamp(150, 0, 100) → 100
        clamp(-5,  0, 100) → 0
        clamp(75,  0, 100) → 75
    """
    return max(min_val, min(value, max_val))


def format_stat_block(character):
    """
    Retorna una representación en texto de las estadísticas
    de un personaje. Útil para logs o debugging.

    Ejemplo de salida:
        "Kael | STR:60 AGI:80 MAG:90 KNW:70"
    """
    return (
        f"{character['name']} | "
        f"STR:{character['strength']} "
        f"AGI:{character['agility']} "
        f"MAG:{character['magic']} "
        f"KNW:{character['knowledge']}"
    )


def is_positive_integer(value):
    """
    Verifica si un valor es un entero positivo (> 0).
    Se usa para validar IDs en las rutas.

    Ejemplo:
        is_positive_integer(5)   → True
        is_positive_integer(0)   → False
        is_positive_integer(-1)  → False
        is_positive_integer("5") → False
    """
    return isinstance(value, int) and value > 0


def success_response(message, data=None, status_code=200):
    """
    Respuesta estándar para operaciones exitosas.

    Ejemplo:
        {
            "success": True,
            "message": "Operación realizada correctamente.",
            "data": {...}
        }
    """
    response = {
        "success": True,
        "message": message,
        "data": data
    }

    return jsonify(response), status_code


def error_response(message, status_code=400, details=None):
    """
    Respuesta estándar para errores.

    Ejemplo:
        {
            "success": False,
            "message": "Descripción del error.",
            "details": {...}
        }
    """
    response = {
        "success": False,
        "message": message
    }

    if details is not None:
        response["details"] = details

    return jsonify(response), status_code