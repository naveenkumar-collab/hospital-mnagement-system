from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"]
)

@router.post("/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db=db, doctor=doctor)

@router.get("/", response_model=List[schemas.Doctor])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db, skip=skip, limit=limit)
    return doctors

@router.get("/{doctor_id}", response_model=schemas.Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@router.put("/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(doctor_id: int, doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = crud.update_doctor(db, doctor_id, doctor)
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@router.delete("/{doctor_id}", response_model=schemas.Doctor)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.delete_doctor(db, doctor_id)
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor
