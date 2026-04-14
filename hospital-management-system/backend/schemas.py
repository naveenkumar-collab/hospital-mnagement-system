from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

# Patient
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int
    class Config:
        from_attributes = True

# Doctor
class DoctorBase(BaseModel):
    name: str
    specialization: str
    phone: str
    experience: int

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_id: int
    class Config:
        from_attributes = True

# Appointment
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: date
    time: time
    status: str

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointment_id: int
    class Config:
        from_attributes = True

# Billing
class BillingBase(BaseModel):
    patient_id: int
    amount: float
    payment_status: str
    date: date

class BillingCreate(BillingBase):
    pass

class Billing(BillingBase):
    bill_id: int
    class Config:
        from_attributes = True
