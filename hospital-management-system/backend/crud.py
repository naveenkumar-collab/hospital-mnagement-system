from sqlalchemy.orm import Session
from . import models, schemas

# Patient
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: int, patient: schemas.PatientCreate):
    db_patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if db_patient:
        for key, value in patient.model_dump().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

# Doctor
def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def update_doctor(db: Session, doctor_id: int, doctor: schemas.DoctorCreate):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()
    if db_doctor:
        for key, value in doctor.model_dump().items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor

# Appointment
def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.model_dump())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def update_appointment(db: Session, appointment_id: int, appointment: schemas.AppointmentCreate):
    db_appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
    if db_appointment:
        for key, value in appointment.model_dump().items():
            setattr(db_appointment, key, value)
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment

# Billing
def get_billing(db: Session, bill_id: int):
    return db.query(models.Billing).filter(models.Billing.bill_id == bill_id).first()

def get_billings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Billing).offset(skip).limit(limit).all()

def create_billing(db: Session, billing: schemas.BillingCreate):
    db_billing = models.Billing(**billing.model_dump())
    db.add(db_billing)
    db.commit()
    db.refresh(db_billing)
    return db_billing

def update_billing(db: Session, bill_id: int, billing: schemas.BillingCreate):
    db_billing = db.query(models.Billing).filter(models.Billing.bill_id == bill_id).first()
    if db_billing:
        for key, value in billing.model_dump().items():
            setattr(db_billing, key, value)
        db.commit()
        db.refresh(db_billing)
    return db_billing

def delete_billing(db: Session, bill_id: int):
    db_billing = db.query(models.Billing).filter(models.Billing.bill_id == bill_id).first()
    if db_billing:
        db.delete(db_billing)
        db.commit()
    return db_billing
