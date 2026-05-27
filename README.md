# 🧋 BubbleTea Store — Backend

API REST desarrollada con **FastAPI** y **MySQL** (Aiven) para gestionar el catálogo de Bubble Teas de la tienda.

---

## 🚀 Tecnologías

- **FastAPI** — framework web moderno para Python
- **pymysql** — conector MySQL
- **Pydantic** — validación de modelos
- **python-dotenv** — gestión de variables de entorno
- **Uvicorn** — servidor ASGI
- **Aiven** — base de datos MySQL en la nube

---

## 📁 Estructura del proyecto

```
backend/
├── app/
│   ├── db/
│   │   └── connection.py   # Conexión a MySQL (Aiven)
│   ├── models/
│   │   └── bubbletea.py    # Modelo Pydantic BubbleTea
│   └── routes/
│       └── bubbleteas.py   # Endpoints CRUD
├── main.py                 # Entrada de la app, CORS, routers
├── .env                    # Variables de entorno (no subir a git)
└── requirements.txt
```

---

## ⚙️ Instalación y arranque

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Mac / Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Arrancar el servidor
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

Documentación automática de FastAPI en `http://localhost:8000/docs`

---

## 🔧 Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=tu-host-aiven
DB_PORT=3306
DB_USER=tu-usuario
DB_PASSWORD=tu-contraseña
DB_NAME=bubbletea_store
```

> ⚠️ Este archivo no debe subirse al repositorio. Añádelo al `.gitignore`.

---

## 📡 Endpoints

Todos los endpoints devuelven el formato:
```json
{ "ok": true, "result": ... }
```

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/bubbleteas` | Obtener todos los productos |
| GET | `/bubbleteas/{id}` | Obtener producto por id |
| POST | `/bubbleteas` | Crear nuevo producto |
| PUT | `/bubbleteas/{id}` | Actualizar producto |
| DELETE | `/bubbleteas/{id}` | Desactivar producto |

---

## 🧋 Modelo BubbleTea

```python
class BubbleTea(BaseModel):
    id: Optional[int] = None
    name: str           # mín. 2, máx. 100 caracteres
    temperature: str    # "hot" | "cold" | "both"
    price: float        # mayor que 0
    active: bool        # True por defecto
```

---

## 🗄️ Base de datos

La base de datos está alojada en **Aiven** (MySQL en la nube). La conexión se realiza con SSL.

Estructura de la tabla:

```sql
CREATE TABLE bubbleteas (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(100) NOT NULL,
  temperature ENUM('hot', 'cold', 'both') NOT NULL,
  price       DECIMAL(10, 2) NOT NULL,
  active      BOOLEAN DEFAULT TRUE,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## 🌐 CORS

Configurado para permitir peticiones desde el frontend Angular:

```python
allow_origins=["http://localhost:4200"]
```
