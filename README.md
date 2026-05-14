# FastAPI Py

Modern REST API built with FastAPI, SQLAlchemy, Docker and PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Features

✅ REST API with FastAPI  
✅ CRUD Operations  
✅ SQLAlchemy ORM  
✅ Pydantic Validation  
✅ Docker & Docker Compose  
✅ Automatic Swagger Documentation  
✅ Clean Project Structure  

---

# Project Structure

```bash
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── app/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    └── crud.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Mehdi-dev74/FastApi-Py.git
cd your-repo
```

## Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

## Local Development

```bash
uvicorn app.main:app --reload
```

Application available at:

```txt
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API docs:

## Swagger UI

```txt
http://127.0.0.1:8000/docs
```

## ReDoc

```txt
http://127.0.0.1:8000/redoc
```

---

# Docker Setup

## Build & Run

```bash
docker-compose up --build
```
---

# Future Improvements

- JWT Authentication
- PostgreSQL Integration
- Unit Testing
- CI/CD Pipeline
- Alembic Migrations
---

