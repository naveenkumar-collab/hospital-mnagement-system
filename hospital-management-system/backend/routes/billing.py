from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/billings",
    tags=["billings"]
)

@router.post("/", response_model=schemas.Billing)
def create_billing(billing: schemas.BillingCreate, db: Session = Depends(get_db)):
    return crud.create_billing(db=db, billing=billing)

@router.get("/", response_model=List[schemas.Billing])
def read_billings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    billings = crud.get_billings(db, skip=skip, limit=limit)
    return billings

@router.get("/{bill_id}", response_model=schemas.Billing)
def read_billing(bill_id: int, db: Session = Depends(get_db)):
    db_billing = crud.get_billing(db, bill_id=bill_id)
    if db_billing is None:
        raise HTTPException(status_code=404, detail="Billing not found")
    return db_billing

@router.put("/{bill_id}", response_model=schemas.Billing)
def update_billing(bill_id: int, billing: schemas.BillingCreate, db: Session = Depends(get_db)):
    db_billing = crud.update_billing(db, bill_id, billing)
    if not db_billing:
        raise HTTPException(status_code=404, detail="Billing not found")
    return db_billing

@router.delete("/{bill_id}", response_model=schemas.Billing)
def delete_billing(bill_id: int, db: Session = Depends(get_db)):
    db_billing = crud.delete_billing(db, bill_id)
    if not db_billing:
        raise HTTPException(status_code=404, detail="Billing not found")
    return db_billing
