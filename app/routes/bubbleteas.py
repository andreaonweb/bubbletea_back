from fastapi import APIRouter
from app.models.bubbletea import BubbleTea
from app.db.connection import get_db_connection

router = APIRouter(prefix="/bubbleteas", tags=["bubbleteas"])


@router.get("")
def get_all():
    conn = get_db_connection()
    if conn is None:
        return {"ok": False, "error": "No se pudo conectar a la base de datos"}
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM bubbleteas")
            rows = cur.fetchall()
            return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        conn.close()


@router.get("/{id}")
def get_by_id(id: int):
    conn = get_db_connection()
    if conn is None:
        return {"ok": False, "error": "No se pudo conectar a la base de datos"}
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM bubbleteas WHERE id = %s", (id,))
            row = cur.fetchone()
            if row is None:
                return {"ok": False, "error": f"No se encontró ningún bubbletea con id {id}"}
            return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        conn.close()


@router.post("")
def create(bubble_tea: BubbleTea):
    conn = get_db_connection()
    if conn is None:
        return {"ok": False, "error": "No se pudo conectar a la base de datos"}
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO bubbleteas (name, temperature, price, active) VALUES (%s, %s, %s, %s)",
                (bubble_tea.name, bubble_tea.temperature, bubble_tea.price, bubble_tea.active)
            )
            conn.commit()
            return {"ok": True, "result": bubble_tea}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        conn.close()


@router.put("/{id}")
def update(id: int, bubble_tea: BubbleTea):
    conn = get_db_connection()
    if conn is None:
        return {"ok": False, "error": "No se pudo conectar a la base de datos"}
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE bubbleteas SET name=%s, temperature=%s, price=%s, active=%s WHERE id=%s",
                (bubble_tea.name, bubble_tea.temperature, bubble_tea.price, bubble_tea.active, id)
            )
            conn.commit()
            return {"ok": True, "result": bubble_tea}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        conn.close()


@router.delete("/{id}")
def delete(id: int):
    conn = get_db_connection()
    if conn is None:
        return {"ok": False, "error": "No se pudo conectar a la base de datos"}
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE bubbleteas SET active = FALSE WHERE id = %s", (id,))
            conn.commit()
            return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        conn.close()