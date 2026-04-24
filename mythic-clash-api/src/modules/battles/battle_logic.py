# Motor de cálculo para las batallas entre personajes.


def calculate_score(character):
    """
    Calcula el puntaje de combate de un personaje según sus estadísticas.
    """
    strength = character["strength"]
    agility = character["agility"]
    magic = character["magic"]
    knowledge = character["knowledge"]

    score = (
        (strength * 0.35)
        + (agility * 0.25)
        + (magic * 0.25)
        + (knowledge * 0.15)
    )

    # Aplica bonificaciones por estadísticas destacadas.
    if strength >= 85:
        score += 5

    if agility >= 85:
        score += 5

    if magic >= 85:
        score += 5

    if knowledge >= 85:
        score += 3

    # Aplica bonificaciones por combinaciones estratégicas.
    if strength >= 70 and agility >= 70:
        score += 4

    if magic >= 70 and knowledge >= 70:
        score += 4

    return round(score, 2)


def determine_victory_type(winner, loser):
    """
    Determina el tipo de victoria según la mayor ventaja estadística.
    """
    differences = {
        "strength": winner["strength"] - loser["strength"],
        "agility": winner["agility"] - loser["agility"],
        "magic": winner["magic"] - loser["magic"],
        "knowledge": winner["knowledge"] - loser["knowledge"],
    }

    dominant_stat = max(differences, key=differences.get)
    dominant_difference = differences[dominant_stat]

    if dominant_difference < 5:
        return "Balanced Win"

    victory_types = {
        "strength": "Brute Force",
        "agility": "Swift Strike",
        "magic": "Arcane Power",
        "knowledge": "Tactical Victory",
    }

    return victory_types[dominant_stat]


def build_summary(winner, loser, victory_type, winner_score, loser_score, tie_broken_by=None):
    """
    Construye el resumen narrativo de la batalla.
    """
    winner_name = winner["name"]
    loser_name = loser["name"]
    margin = round(abs(winner_score - loser_score), 2)

    if tie_broken_by == "knowledge":
        return (
            f"{winner_name} won a very close battle against {loser_name}. "
            f"Both fighters had the same score, but higher knowledge gave "
            f"{winner_name} the strategic advantage."
        )

    if tie_broken_by == "agility":
        return (
            f"{winner_name} defeated {loser_name} in an extremely close battle. "
            f"The tie was decided by superior agility and faster reaction speed."
        )

    summaries = {
        "Brute Force": (
            f"{winner_name} defeated {loser_name} with superior physical strength. "
            f"Raw power was the key factor in the battle."
        ),
        "Swift Strike": (
            f"{winner_name} overcame {loser_name} with superior agility. "
            f"Fast movement and precise attacks defined the fight."
        ),
        "Arcane Power": (
            f"{winner_name} defeated {loser_name} through strong magical control. "
            f"Special attacks made the difference."
        ),
        "Tactical Victory": (
            f"{winner_name} defeated {loser_name} through knowledge and better strategy. "
            f"Smarter decisions gave the winner a clear advantage."
        ),
        "Balanced Win": (
            f"{winner_name} defeated {loser_name} in a balanced battle. "
            f"The final difference was {margin} points."
        ),
    }

    return summaries.get(
        victory_type,
        f"{winner_name} defeated {loser_name}."
    )


def resolve_battle(character1, character2):
    """
    Resuelve una batalla y retorna el resultado estructurado.
    """
    score1 = calculate_score(character1)
    score2 = calculate_score(character2)

    tie_broken_by = None

    if score1 > score2:
        winner = character1
        loser = character2
        winner_score = score1
        loser_score = score2

    elif score2 > score1:
        winner = character2
        loser = character1
        winner_score = score2
        loser_score = score1

    else:
        # Aplica el primer criterio de desempate.
        if character1["knowledge"] > character2["knowledge"]:
            winner = character1
            loser = character2
            tie_broken_by = "knowledge"

        elif character2["knowledge"] > character1["knowledge"]:
            winner = character2
            loser = character1
            tie_broken_by = "knowledge"

        else:
            # Aplica el segundo criterio de desempate.
            if character1["agility"] >= character2["agility"]:
                winner = character1
                loser = character2
            else:
                winner = character2
                loser = character1

            tie_broken_by = "agility"

        winner_score = score1
        loser_score = score2

    victory_type = determine_victory_type(winner, loser)

    summary = build_summary(
        winner,
        loser,
        victory_type,
        winner_score,
        loser_score,
        tie_broken_by
    )

    return {
        "winner": {
            "id": winner["id"],
            "name": winner["name"],
            "race": winner["race"],
            "score": winner_score,
        },
        "loser": {
            "id": loser["id"],
            "name": loser["name"],
            "race": loser["race"],
            "score": loser_score,
        },
        "scores": {
            character1["name"]: score1,
            character2["name"]: score2,
        },
        "victory_type": victory_type,
        "tie_broken_by": tie_broken_by,
        "summary": summary,
    }