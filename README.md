# BubbleTea Store — Backend

API REST desarrollada con FastAPI, SQLAlchemy y MySQL (Aiven). Autenticación mediante Firebase Admin SDK.

## Capturas

### Base de datos — tabla bubbleteas
<img width="621" height="211" alt="image" src="https://github.com/user-attachments/assets/ab3c86e6-ac82-435d-9dbf-1ca50dac81dc" />


### Base de datos — tabla users
<img width="896" height="117" alt="image" src="https://github.com/user-attachments/assets/1f9ccecd-1048-4c58-ae28-9b209b54f2dd" />


### Endpoints en Swagger
<img width="1399" height="802" alt="image" src="https://github.com/user-attachments/assets/d723a4e4-f04e-40d9-8cf7-6fb8a0c90a65" />
<br>
<img width="1400" height="659" alt="image" src="https://github.com/user-attachments/assets/53684ddf-a67e-44e4-be61-485b29cb4232" />
<br>
<img width="1398" height="700" alt="image" src="https://github.com/user-attachments/assets/9fd15e08-e3d6-456f-b6f3-cc4f0e3f2a95" />
<br>
<img width="1399" height="539" alt="image" src="https://github.com/user-attachments/assets/b69f13d2-8ed0-4d9f-b150-3879ba03889e" />
<br>
<img width="1392" height="371" alt="image" src="https://github.com/user-attachments/assets/a993918b-df9a-43b9-8265-7538f46954ce" />
<br>
<img width="1386" height="485" alt="image" src="https://github.com/user-attachments/assets/288f57a9-971a-43f7-be33-d29b11daef9e" />



## Tecnologías

- Python + FastAPI
- SQLAlchemy + PyMySQL
- MySQL en Aiven Cloud
- Firebase Admin SDK (verificación de tokens JWT)

## Estructura

```
backend/
├── app/
│   ├── db/
│   │   └── connection.py       # Conexión a Aiven MySQL
│   ├── models/
│   │   ├── bubbletea.py        # ORM + Pydantic BubbleTea
│   │   └── user.py             # ORM User con uid Firebase
│   ├── routes/
│   │   ├── bubbleteas.py       # CRUD Bubble Tea
│   │   └── users.py            # API usuarios protegida
│   └── auth.py                 # Verificación token Firebase
├── main.py
├── requirements.txt
└── .env
```

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz:

```env
DB_HOST=...
DB_PORT=...
DB_USER=...
DB_PASSWORD=...
DB_NAME=...
```

Coloca el archivo `serviceAccount.json` de Firebase en `app/secrets/`.

## Arrancar

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`. Documentación automática en `http://localhost:8000/docs`.

## Endpoints principales

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| GET | /bubbleteas | ✓ | Listar todos |
| GET | /bubbleteas/{id} | ✓ | Obtener por id |
| POST | /bubbleteas | ✓ | Crear |
| PUT | /bubbleteas/{id} | ✓ | Actualizar |
| DELETE | /bubbleteas/{id} | ✓ | Desactivar (soft delete) |
| GET | /users/me | ✓ | Obtener usuario actual |
| POST | /users | ✓ | Crear usuario tras registro |
