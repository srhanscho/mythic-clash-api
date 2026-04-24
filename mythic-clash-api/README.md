# Mythic Clash API

Mythic Clash API es una API REST construida con **Python, Flask y SQLite** para gestionar personajes de un juego RPG y simular batallas estratégicas entre ellos.

Este proyecto fue desarrollado con fines académicos para practicar conceptos de backend, APIs REST, operaciones CRUD, persistencia de datos y lógica de negocio.

---

## Estructura del proyecto

```text
mythic-clash-api/
├── README.md
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
| `routes` | Recibe solicitudes HTTP y retorna respuestas JSON. |
| `service` | Aplica validaciones y reglas de negocio. |
| `repository` | Gestiona el acceso directo a la base de datos. |
| `logic` | Ejecuta los cálculos del sistema de batalla. |
| `utils` | Contiene funciones auxiliares reutilizables. |

---

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- JSON
- REST API

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/srhanscho/mythic-clash-api.git
cd mythic-clash-api
```

> Si el proyecto está dentro de una carpeta interna llamada `mythic-clash-api`, entra a esa carpeta antes de ejecutar los comandos.

---

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

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

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
| GET | `/` | Retorna información general de la API. |

---

## Personajes

Base path:

```text
/characters
```

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/characters` | Lista todos los personajes. |
| GET | `/characters/<id>` | Consulta un personaje por ID. |
| POST | `/characters` | Crea un nuevo personaje. |
| PUT | `/characters/<id>` | Actualiza un personaje existente. |
| DELETE | `/characters/<id>` | Elimina un personaje. |

---

## Modelo de personaje

Cada personaje contiene los siguientes campos:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer | Identificador único del personaje. |
| `name` | String | Nombre del personaje. |
| `skin_color` | String | Color de piel del personaje. |
| `race` | String | Raza del personaje. |
| `strength` | Integer | Nivel de fuerza. |
| `agility` | Integer | Nivel de agilidad. |
| `magic` | Integer | Nivel de magia. |
| `knowledge` | Integer | Nivel de conocimiento. |

Las estadísticas deben ser números enteros entre `0` y `100`.

Ejemplo:

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
| POST | `/battle` | Ejecuta una batalla entre dos personajes. |

---

## Ejecutar batalla

### Request

```http
POST /battle
```

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
        "score": 64.25
      },
      "scores": {
        "Kael": 83.0,
        "Theron": 64.25
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
| `Brute Force` | Ventaja dominante en fuerza. |
| `Arcane Power` | Ventaja dominante en magia. |
| `Swift Strike` | Ventaja dominante en agilidad. |
| `Tactical Victory` | Ventaja dominante en conocimiento. |
| `Balanced Win` | Sin ventaja estadística clara. |

### Reglas de desempate

Si ambos personajes obtienen el mismo puntaje:

1. Gana quien tenga mayor `knowledge`.
2. Si continúa el empate, gana quien tenga mayor `agility`.

---

## Ejemplos de prueba con PowerShell

### Crear personaje

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/characters" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"name":"Kael","skin_color":"pale","race":"Elf","strength":60,"agility":80,"magic":90,"knowledge":70}' | ConvertTo-Json -Depth 10
```

### Crear segundo personaje

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/characters" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"name":"Theron","skin_color":"fair","race":"Human","strength":75,"agility":65,"magic":45,"knowledge":70}' | ConvertTo-Json -Depth 10
```

### Listar personajes

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/characters" -Method GET | ConvertTo-Json -Depth 10
```

### Consultar personaje por ID

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/characters/1" -Method GET | ConvertTo-Json -Depth 10
```

### Actualizar personaje

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/characters/1" `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"name":"Kael","skin_color":"pale","race":"Elf","strength":65,"agility":82,"magic":95,"knowledge":75}' | ConvertTo-Json -Depth 10
```

### Ejecutar batalla

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/battle" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"character1_id":1,"character2_id":2}' | ConvertTo-Json -Depth 10
```

### Eliminar personaje

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/characters/1" -Method DELETE | ConvertTo-Json -Depth 10
```

---

## Códigos de respuesta HTTP

| Código | Significado |
|---|---|
| `200` | Operación exitosa. |
| `201` | Recurso creado. |
| `400` | Datos inválidos o incompletos. |
| `404` | Recurso no encontrado. |
| `405` | Método HTTP no permitido. |
| `409` | Conflicto por datos duplicados. |
| `500` | Error interno del servidor. |

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

- Crear personajes RPG.
- Listar personajes registrados.
- Consultar personajes por ID.
- Actualizar personajes existentes.
- Eliminar personajes.
- Validar datos de entrada.
- Almacenar información en SQLite.
- Ejecutar batallas entre dos personajes existentes.
- Calcular puntajes según estadísticas.
- Determinar un ganador.
- Retornar detalles del resultado de combate.

---

## Estado del proyecto

Proyecto funcional para fines académicos.

---

## Autor

Han's De Ávila Sánchez
2026