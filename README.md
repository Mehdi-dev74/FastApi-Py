# FastAPI Py

Modern REST API built with FastAPI, SQLModel, Docker and JWT authentication.

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-blue)](https://www.docker.com/)

---

# Features

✅ REST API with FastAPI  
✅ Async SQLModel / SQLite  
✅ Pydantic Validation  
✅ JWT Authentication (login token)  
✅ Password hashing with bcrypt  
✅ Docker / Docker Compose  
✅ Swagger UI auto-generated docs  

---

# Project Structure

```bash
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── app/
    ├── core/
    │   └── config.py
    ├── database.py
    ├── main.py
    ├── models.py
    ├── schemas.py
    ├── security.py
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
venv\Scripts\activate
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

# Authentication

- Create a user: `POST /users/`
- Get a token: `POST /token`

The app now hashes passwords and issues a bearer token for login.

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

# Environment

The service reads environment variables from `.env` when present. You can copy `.env.example` to `.env` and customize values.

- `DATABASE_URL` - database connection string
- `SECRET_KEY` - JWT secret

---

# Notes

- The app uses `sqlite+aiosqlite` by default for easy local development.
- The database file is created automatically on startup.
---
