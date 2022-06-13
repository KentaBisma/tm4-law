from pydantic import BaseModel


class MahasiswaBase(BaseModel):
    nama: str
    npm: int


class MahasiswaCreate(MahasiswaBase):
    pass

class Mahasiswa(MahasiswaBase):

    class Config:
        orm_mode = True
