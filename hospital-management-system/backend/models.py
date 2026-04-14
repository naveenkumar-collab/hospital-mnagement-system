from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String)
    address = Column(String)

    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete")
    bills = relationship("Billing", back_populates="patient", cascade="all, delete")

class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)
    phone = Column(String)
    experience = Column(Integer)

    appointments = relationship("Appointment", back_populates="doctor", cascade="all, delete")

class Appointment(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"))
    date = Column(Date)
    time = Column(Time)
    status = Column(String, default="Scheduled")

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

class Billing(Base):
    __tablename__ = "billings"

    bill_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    amount = Column(Float)
    payment_status = Column(String, default="Pending")
    date = Column(Date)

    patient = relationship("Patient", back_populates="bills")
