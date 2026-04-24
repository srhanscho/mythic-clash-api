import sys
import os

# Configura la resolución de módulos locales.
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, jsonify
from config.db import init_db
from modules.characters.character_routes import characters_bp
from modules.battles.battle_routes import battles_bp


app = Flask(__name__)

# Asegura la disponibilidad del esquema de base de datos.
init_db()

# Registra los módulos principales de la aplicación.
app.register_blueprint(characters_bp)
app.register_blueprint(battles_bp)


@app.route("/")
def index():
    """Endpoint de verificación y metadatos de la API."""
    return jsonify({
        "success": True,
        "message": "Mythic Clash API is running successfully.",
        "data": {
            "api": "Mythic Clash API",
            "version": "1.0.0",
            "status": "running",
            "endpoints": {
                "characters": "/characters",
                "battle": "/battle"
            }
        }
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Gestiona rutas no encontradas."""
    return jsonify({
        "success": False,
        "message": "Route not found."
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Gestiona métodos HTTP no permitidos."""
    return jsonify({
        "success": False,
        "message": "HTTP method not allowed for this route."
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Gestiona errores internos inesperados."""
    return jsonify({
        "success": False,
        "message": "Internal server error."
    }), 500


if __name__ == "__main__":
    print("Starting Mythic Clash API...")
    print("Server available at: http://127.0.0.1:5000")

    # Configuración del servidor de desarrollo.
    app.run(debug=True, port=5000)