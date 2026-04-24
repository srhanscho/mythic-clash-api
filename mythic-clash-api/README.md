# Mythic Clash API

API REST construida con **Python, Flask y SQLite** para gestionar personajes de un juego RPG y simular batallas estratégicas entre ellos.

Proyecto académico orientado al aprendizaje de APIs REST, operaciones CRUD y lógica de negocio aplicada.

---

## Estructura del proyecto

```text
mythic-clash-api/
│
├── requirements.txt
└── src/
    ├── main.py
    ├── config/
    │   └── db.py
    ├── modules/
    │   ├── characters/
    │   │   ├── character_routes.py
    │   │   ├── character_service.py
    │   │   └── character_repository.py
    │   └── battles/
    │       ├── battle_routes.py
    │       ├── battle_service.py
    │       └── battle_logic.py
    └── utils/
        └── helpers.py
```

---

## Arquitectura

| Capa | Responsabilidad |
|---|---|
| `routes` | Recibe solicitudes HTTP y retorna respuestas JSON |
| `service` | Aplica validaciones y reglas de negocio |
| `repository` | Gestiona el acceso directo a la base de datos |
| `logic` | Ejecuta cálculos puros del sistema de batalla |
| `utils` | Contiene funciones auxiliares reutilizables |

---

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- JSON
- REST API

---

## Instalación y ejecución

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd mythic-clash-api
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar en Windows:

```bash
venv\Scripts\activate
```

Activar en Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API

```bash
cd src
python main.py
```

La API estará disponible en:

```text
http://127.0.0.1:5000
```

La base de datos `database.db` se crea automáticamente al iniciar la aplicación.

---

## Endpoints disponibles

### Información general

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Retorna información general de la API |

---

## Personajes

Base path:

```text
/characters
```

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/characters` | Lista todos los personajes |
| GET | `/characters/<id>` | Consulta un personaje por ID |
| POST | `/characters` | Crea un nuevo personaje |
| PUT | `/characters/<id>` | Actualiza un personaje existente |
| DELETE | `/characters/<id>` | Elimina un personaje |

### Modelo de personaje

```json
{
  "id": 1,
  "name": "Kael",
  "skin_color": "pale",
  "race": "Elf",
  "strength": 60,
  "agility": 80,
  "magic": 90,
  "knowledge": 70
}
```

Las estadísticas deben ser números enteros entre `0` y `100`.

---

## Crear personaje

### Request

```http
POST /characters
```

```json
{
  "name": "Kael",
  "skin_color": "pale",
  "race": "Elf",
  "strength": 60,
  "agility": 80,
  "magic": 90,
  "knowledge": 70
}
```

### Response

```json
{
  "success": true,
  "message": "Character created successfully.",
  "data": {
    "character": {
      "id": 1,
      "name": "Kael",
      "skin_color": "pale",
      "race": "Elf",
      "strength": 60,
      "agility": 80,
      "magic": 90,
      "knowledge": 70
    }
  }
}
```

---

## Listar personajes

### Request

```http
GET /characters
```

### Response

```json
{
  "success": true,
  "message": "Characters retrieved successfully.",
  "data": {
    "characters": [
      {
        "id": 1,
        "name": "Kael",
        "skin_color": "pale",
        "race": "Elf",
        "strength": 60,
        "agility": 80,
        "magic": 90,
        "knowledge": 70
      }
    ],
    "total": 1
  }
}
```

---

## Consultar personaje por ID

### Request

```http
GET /characters/1
```

### Response

```json
{
  "success": true,
  "message": "Character retrieved successfully.",
  "data": {
    "character": {
      "id": 1,
      "name": "Kael",
      "skin_color": "pale",
      "race": "Elf",
      "strength": 60,
      "agility": 80,
      "magic": 90,
      "knowledge": 70
    }
  }
}
```

---

## Actualizar personaje

### Request

```http
PUT /characters/1
```

```json
{
  "name": "Kael",
  "skin_color": "pale",
  "race": "Elf",
  "strength": 65,
  "agility": 82,
  "magic": 95,
  "knowledge": 75
}
```

### Response

```json
{
  "success": true,
  "message": "Character updated successfully.",
  "data": {
    "character": {
      "id": 1,
      "name": "Kael",
      "skin_color": "pale",
      "race": "Elf",
      "strength": 65,
      "agility": 82,
      "magic": 95,
      "knowledge": 75
    }
  }
}
```

---

## Eliminar personaje

### Request

```http
DELETE /characters/1
```

### Response

```json
{
  "success": true,
  "message": "Character 'Kael' deleted successfully.",
  "data": null
}
```

---

## Batallas

Base path:

```text
/battle
```

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/battle` | Ejecuta una batalla entre dos personajes |

### Request

```json
{
  "character1_id": 1,
  "character2_id": 2
}
```

### Response

```json
{
  "success": true,
  "message": "Battle resolved successfully.",
  "data": {
    "combatants": {
      "character1": {
        "id": 1,
        "name": "Kael"
      },
      "character2": {
        "id": 2,
        "name": "Theron"
      }
    },
    "result": {
      "winner": {
        "id": 1,
        "name": "Kael",
        "race": "Elf",
        "score": 83.0
      },
      "loser": {
        "id": 2,
        "name": "Theron",
        "race": "Human",
        "score": 69.3
      },
      "scores": {
        "Kael": 83.0,
        "Theron": 69.3
      },
      "victory_type": "Arcane Power",
      "tie_broken_by": null,
      "summary": "Kael defeated Theron through strong magical control. Special attacks made the difference."
    }
  }
}
```

---

## Lógica de batalla

Cada personaje recibe un puntaje de combate calculado con la siguiente fórmula:

```text
score = (strength * 0.35) + (agility * 0.25) + (magic * 0.25) + (knowledge * 0.15)
```

### Bonificaciones individuales

| Condición | Bonus |
|---|---|
| `strength >= 85` | `+5` |
| `agility >= 85` | `+5` |
| `magic >= 85` | `+5` |
| `knowledge >= 85` | `+3` |

### Bonificaciones combinadas

| Condición | Bonus |
|---|---|
| `strength >= 70` y `agility >= 70` | `+4` |
| `magic >= 70` y `knowledge >= 70` | `+4` |

### Tipos de victoria

| Tipo | Criterio |
|---|---|
| `Brute Force` | Ventaja dominante en fuerza |
| `Arcane Power` | Ventaja dominante en magia |
| `Swift Strike` | Ventaja dominante en agilidad |
| `Tactical Victory` | Ventaja dominante en conocimiento |
| `Balanced Win` | Sin ventaja estadística clara |

### Reglas de desempate

Si ambos personajes obtienen el mismo puntaje:

1. Gana quien tenga mayor `knowledge`.
2. Si continúa el empate, gana quien tenga mayor `agility`.

---

## Ejemplos de prueba con curl

### Crear personaje

```bash
curl -X POST http://127.0.0.1:5000/characters \
  -H "Content-Type: application/json" \
  -d '{"name":"Kael","skin_color":"pale","race":"Elf","strength":60,"agility":80,"magic":90,"knowledge":70}'
```

### Crear segundo personaje

```bash
curl -X POST http://127.0.0.1:5000/characters \
  -H "Content-Type: application/json" \
  -d '{"name":"Theron","skin_color":"fair","race":"Human","strength":75,"agility":65,"magic":45,"knowledge":70}'
```

### Listar personajes

```bash
curl http://127.0.0.1:5000/characters
```

### Consultar personaje por ID

```bash
curl http://127.0.0.1:5000/characters/1
```

### Actualizar personaje

```bash
curl -X PUT http://127.0.0.1:5000/characters/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Kael","skin_color":"pale","race":"Elf","strength":65,"agility":82,"magic":95,"knowledge":75}'
```

### Ejecutar batalla

```bash
curl -X POST http://127.0.0.1:5000/battle \
  -H "Content-Type: application/json" \
  -d '{"character1_id":1,"character2_id":2}'
```

### Eliminar personaje

```bash
curl -X DELETE http://127.0.0.1:5000/characters/1
```

---

## Códigos de respuesta HTTP

| Código | Significado |
|---|---|
| `200` | Operación exitosa |
| `201` | Recurso creado |
| `400` | Datos inválidos o incompletos |
| `404` | Recurso no encontrado |
| `405` | Método HTTP no permitido |
| `409` | Conflicto por datos duplicados |
| `500` | Error interno del servidor |

---

## Formato estándar de respuesta

### Respuesta exitosa

```json
{
  "success": true,
  "message": "Operation completed successfully.",
  "data": {}
}
```

### Respuesta con error

```json
{
  "success": false,
  "message": "Error description.",
  "details": {}
}
```

---

## Alcance del proyecto

La API permite:

- Crear, consultar, actualizar y eliminar personajes RPG.
- Validar datos de entrada.
- Almacenar información en SQLite.
- Ejecutar batallas entre dos personajes existentes.
- Calcular puntajes según estadísticas.
- Determinar un ganador.
- Retornar detalles del resultado de combate.

---

## Autor

Han's de Ávila Sánchez
2026
