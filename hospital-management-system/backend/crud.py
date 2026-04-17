import json
from bson import ObjectId
from pymongo.database import Database
from . import schemas


def serialize(obj):
    return json.loads(obj.model_dump_json())


def map_patient(doc):
    if not doc:
        return None
    doc["patient_id"] = str(doc.pop("_id"))
    return doc


def map_doctor(doc):
    if not doc:
        return None
    doc["doctor_id"] = str(doc.pop("_id"))
    return doc


def map_appointment(doc):
    if not doc:
        return None
    doc["appointment_id"] = str(doc.pop("_id"))
    return doc


def map_billing(doc):
    if not doc:
        return None
    doc["bill_id"] = str(doc.pop("_id"))
    return doc


# Patient
def get_patient(db: Database, patient_id: str):
    return map_patient(db.patients.find_one({"_id": ObjectId(patient_id)}))


def get_patients(db: Database, skip: int = 0, limit: int = 100):
    return [map_patient(doc) for doc in db.patients.find().skip(skip).limit(limit)]


def create_patient(db: Database, patient: schemas.PatientCreate):
    data = serialize(patient)
    result = db.patients.insert_one(data)
    data["_id"] = result.inserted_id
    return map_patient(data)


def update_patient(db: Database, patient_id: str, patient: schemas.PatientCreate):
    db.patients.update_one(
        {"_id": ObjectId(patient_id)}, {"$set": serialize(patient)}
    )
    return get_patient(db, patient_id)


def delete_patient(db: Database, patient_id: str):
    doc = get_patient(db, patient_id)
    if doc:
        db.patients.delete_one({"_id": ObjectId(patient_id)})
    return doc


# Doctor
def get_doctor(db: Database, doctor_id: str):
    return map_doctor(db.doctors.find_one({"_id": ObjectId(doctor_id)}))


def get_doctors(db: Database, skip: int = 0, limit: int = 100):
    return [map_doctor(doc) for doc in db.doctors.find().skip(skip).limit(limit)]


def create_doctor(db: Database, doctor: schemas.DoctorCreate):
    data = serialize(doctor)
    result = db.doctors.insert_one(data)
    data["_id"] = result.inserted_id
    return map_doctor(data)


def update_doctor(db: Database, doctor_id: str, doctor: schemas.DoctorCreate):
    db.doctors.update_one(
        {"_id": ObjectId(doctor_id)}, {"$set": serialize(doctor)}
    )
    return get_doctor(db, doctor_id)


def delete_doctor(db: Database, doctor_id: str):
    doc = get_doctor(db, doctor_id)
    if doc:
        db.doctors.delete_one({"_id": ObjectId(doctor_id)})
    return doc


# Appointment
def get_appointment(db: Database, appointment_id: str):
    return map_appointment(db.appointments.find_one({"_id": ObjectId(appointment_id)}))


def get_appointments(db: Database, skip: int = 0, limit: int = 100):
    return [
        map_appointment(doc) for doc in db.appointments.find().skip(skip).limit(limit)
    ]


def create_appointment(db: Database, appointment: schemas.AppointmentCreate):
    data = serialize(appointment)
    result = db.appointments.insert_one(data)
    data["_id"] = result.inserted_id
    return map_appointment(data)


def update_appointment(
    db: Database, appointment_id: str, appointment: schemas.AppointmentCreate
):
    db.appointments.update_one(
        {"_id": ObjectId(appointment_id)}, {"$set": serialize(appointment)}
    )
    return get_appointment(db, appointment_id)


def delete_appointment(db: Database, appointment_id: str):
    doc = get_appointment(db, appointment_id)
    if doc:
        db.appointments.delete_one({"_id": ObjectId(appointment_id)})
    return doc


# Billing
def get_billing(db: Database, bill_id: str):
    return map_billing(db.billings.find_one({"_id": ObjectId(bill_id)}))


def get_billings(db: Database, skip: int = 0, limit: int = 100):
    return [map_billing(doc) for doc in db.billings.find().skip(skip).limit(limit)]


def create_billing(db: Database, billing: schemas.BillingCreate):
    data = serialize(billing)
    result = db.billings.insert_one(data)
    data["_id"] = result.inserted_id
    return map_billing(data)


def update_billing(db: Database, bill_id: str, billing: schemas.BillingCreate):
    db.billings.update_one({"_id": ObjectId(bill_id)}, {"$set": serialize(billing)})
    return get_billing(db, bill_id)


def delete_billing(db: Database, bill_id: str):
    doc = get_billing(db, bill_id)
    if doc:
        db.billings.delete_one({"_id": ObjectId(bill_id)})
    return doc
