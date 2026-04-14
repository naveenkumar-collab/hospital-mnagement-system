from fastapi import APIRouter, Depends, HTTPException
from pymongo.database import Database
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)

@router.post("/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Database = Depends(get_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@router.get("/", response_model=List[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Database = Depends(get_db)):
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@router.get("/{appointment_id}", response_model=schemas.Appointment)
def read_appointment(appointment_id: str, db: Database = Depends(get_db)):
    db_appointment = crud.get_appointment(db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.put("/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: str, appointment: schemas.AppointmentCreate, db: Database = Depends(get_db)):
    db_appointment = crud.update_appointment(db, appointment_id, appointment)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@router.delete("/{appointment_id}", response_model=schemas.Appointment)
def delete_appointment(appointment_id: str, db: Database = Depends(get_db)):
    db_appointment = crud.delete_appointment(db, appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment
