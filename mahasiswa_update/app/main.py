import os
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/update/", response_model=schemas.Mahasiswa)
def create_mahasiswa(mhsw: schemas.MahasiswaCreate, db: Session = Depends(get_db)):
    db_mhsw = crud.get_mahasiswa(db, npm=mhsw.npm)
    if db_mhsw:
        raise HTTPException(status_code=400, detail="NPM sudah ada")
    return crud.create_mahasiswa(db=db, mhsw=mhsw)

# Update
@app.put("/update/", response_model=schemas.Mahasiswa)
def update_mahasiswa(mhsw: schemas.MahasiswaUpdate, db: Session = Depends(get_db)):
    db_mhsw = crud.get_mahasiswa(db, npm=mhsw.npm)
    if db_mhsw is None:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return crud.update_mahasiswa(db, mhsw)