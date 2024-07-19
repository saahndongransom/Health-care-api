

# Healthcare Management System

## Overview

The Healthcare Management System is a Django-based web application designed for managing patient information, medical records, appointments, and prescriptions. It provides functionalities to create, read, update, and delete patient records, manage appointments, and keep track of medical prescriptions.

## Features

- **Patient Management:** Add, update, view, and delete patient information.
- **Medical Records:** Create and manage medical records for each patient.
- **Appointments:** Schedule and manage patient appointments.
- **Prescriptions:** Record and track prescriptions for patients.
- **User Authentication:** Secure login and user management.

## Technologies Used

- **Django:** A high-level Python web framework for rapid development.
- **Django REST Framework:** Toolkit for building Web APIs.
- **PostgreSQL:** Database options .

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x+
- Django REST Framework


7. **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## API Endpoints

### Patients

- **List all patients**
  - `GET /api/patients/`
- **Retrieve a single patient**
  - `GET /api/patients/{id}/`
- **Create a new patient**
  - `POST /api/patients/`
- **Update a patient**
  - `PUT /api/patients/{id}/`
- **Delete a patient**
  - `DELETE /api/patients/{id}/`

### Medical Records

- **List all medical records**
  - `GET /api/medical_records/`
- **Retrieve a single medical record**
  - `GET /api/medical_records/{id}/`
- **Create a new medical record**
  - `POST /api/medical_records/`
- **Update a medical record**
  - `PUT /api/medical_records/{id}/`
- **Delete a medical record**
  - `DELETE /api/medical_records/{id}/`

### Appointments

- **List all appointments**
  - `GET /api/appointments/`
- **Retrieve a single appointment**
  - `GET /api/appointments/{id}/`
- **Create a new appointment**
  - `POST /api/appointments/`
- **Update an appointment**
  - `PUT /api/appointments/{id}/`
- **Delete an appointment**
  - `DELETE /api/appointments/{id}/`

### Prescriptions

- **List all prescriptions**
  - `GET /api/prescriptions/`
- **Retrieve a single prescription**
  - `GET /api/prescriptions/{id}/`
- **Create a new prescription**
  - `POST /api/prescriptions/`
- **Update a prescription**
  - `PUT /api/prescriptions/{id}/`
- **Delete a prescription**
  - `DELETE /api/prescriptions/{id}/`

## Running Tests

To run the test suite, use:
```bash
python manage.py test
```
