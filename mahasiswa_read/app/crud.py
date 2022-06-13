from sqlalchemy.orm import Session

from . import models, schemas


def get_mahasiswa(db: Session, npm: int):
    return db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()


def create_mahasiswa(db: Session, mhsw: schemas.MahasiswaCreate):
    db_mhsw = models.Mahasiswa(nama=mhsw.nama, npm=mhsw.npm)
    db.add(db_mhsw)
    db.commit()
    db.refresh(db_mhsw)
    return db_mhsw
