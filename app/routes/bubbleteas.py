from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.bubbletea import BubbleTea, BubbleTeaORM
from app.db.connection import get_db

router = APIRouter(prefix="/bubbleteas", tags=["bubbleteas"])


@router.get("")
def get_all(db: Session = Depends(get_db)):
    rows = db.query(BubbleTeaORM).all()
    return {"ok": True, "result": rows}


@router.get("/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    row = db.query(BubbleTeaORM).filter(BubbleTeaORM.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail=f"No se encontró ningún bubbletea con id {id}")
    return {"ok": True, "result": row}


@router.post("")
def create(bubble_tea: BubbleTea, db: Session = Depends(get_db)):
    new_bt = BubbleTeaORM(**bubble_tea.model_dump(exclude={"id"}))
    db.add(new_bt)
    db.commit()
    db.refresh(new_bt)
    return {"ok": True, "result": new_bt}


@router.put("/{id}")
def update(id: int, bubble_tea: BubbleTea, db: Session = Depends(get_db)):
    row = db.query(BubbleTeaORM).filter(BubbleTeaORM.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail=f"No se encontró ningún bubbletea con id {id}")
    for key, value in bubble_tea.model_dump(exclude={"id"}).items():
        setattr(row, key, value)
    db.commit()
    db.refresh(row)
    return {"ok": True, "result": row}


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    row = db.query(BubbleTeaORM).filter(BubbleTeaORM.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail=f"No se encontró ningún bubbletea con id {id}")
    row.active = False
    db.commit()
    return {"ok": True}