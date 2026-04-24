import sqlite3
import os

# Define la ubicación del archivo de base de datos.
DB_PATH = os.path.join(os.path.dirname(__file__), "../../database.db")


def get_connection():
    """Crea una conexión activa con la base de datos SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Inicializa el esquema de base de datos requerido por la aplicación."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS characters (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            skin_color  TEXT    NOT NULL,
            race        TEXT    NOT NULL,
            strength    INTEGER NOT NULL DEFAULT 0,
            agility     INTEGER NOT NULL DEFAULT 0,
            magic       INTEGER NOT NULL DEFAULT 0,
            knowledge   INTEGER NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")