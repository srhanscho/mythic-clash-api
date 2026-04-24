from config.db import get_connection


def find_all():
    """Consulta todos los personajes registrados."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM characters")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def find_by_id(character_id):
    """Consulta un personaje por identificador."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM characters WHERE id = ?", (character_id,))
    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def find_by_name(name):
    """Consulta un personaje por nombre."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM characters WHERE LOWER(name) = LOWER(?)",
        (name,)
    )
    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def insert(name, skin_color, race, strength, agility, magic, knowledge):
    """Registra un nuevo personaje."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO characters (
            name,
            skin_color,
            race,
            strength,
            agility,
            magic,
            knowledge
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (name, skin_color, race, strength, agility, magic, knowledge),
    )

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return new_id


def update(character_id, name, skin_color, race, strength, agility, magic, knowledge):
    """Actualiza los datos de un personaje registrado."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE characters
        SET
            name = ?,
            skin_color = ?,
            race = ?,
            strength = ?,
            agility = ?,
            magic = ?,
            knowledge = ?
        WHERE id = ?
        """,
        (name, skin_color, race, strength, agility, magic, knowledge, character_id),
    )

    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()

    return rows_affected > 0


def delete(character_id):
    """Elimina un personaje registrado."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM characters WHERE id = ?", (character_id,))

    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()

    return rows_affected > 0