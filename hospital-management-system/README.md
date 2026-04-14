# Hospital Management System

A full-stack, dynamic Hospital Management System built with FastAPI, SQLite, and a customized HTML/CSS/JS frontend.

## Features

- **Patient Management:** Add, view, update, delete patients.
- **Doctor Management:** Manage doctor details and specialties.
- **Appointment Management:** Schedule and track patient appointments.
- **Billing Module:** Create and manage patient bills.
- **Dashboard:** Overview of hospital statistics.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** HTML5, CSS3 (Modern UI), JavaScript (Vanilla Fetch API)

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python installed. Navigate to the project root directory in your terminal and install dependencies from the `requirements.txt` file (you may want to use a virtual environment):
```bash
pip install -r requirements.txt
```

### 2. Run the Backend Server
Start the FastAPI application using Uvicorn:
```bash
uvicorn backend.main:app --reload
```
The server will start at `http://localhost:8000`. You can also view the interactive API documentation at `http://localhost:8000/docs`.

### 3. Open the Frontend
Since the frontend uses vanilla HTML/JS with API calls to `localhost:8000`, you can simply double-click `frontend/index.html` to open it in your web browser. 
Alternatively, use an extension like "Live Server" in VS Code to run the frontend for a better development experience.

Enjoy managing the hospital!
