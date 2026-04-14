from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routes import patient, doctor, appointment, billing

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(appointment.router)
app.include_router(billing.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hospital Management System API"}
