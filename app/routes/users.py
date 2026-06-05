from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import UserORM
from app.db.connection import get_db
from app.auth import verify_token

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def get_me(token=Depends(verify_token), db: Session = Depends(get_db)):
    user = db.query(UserORM).filter(UserORM.id == token["uid"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"ok": True, "result": user}

@router.post("")
def create_user(data: dict, db: Session = Depends(get_db)):
    user = UserORM(**data)
    db.add(user); db.commit(); db.refresh(user)
    return {"ok": True, "result": user}