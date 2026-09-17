import os

import psycopg
from fastapi import FastAPI

app = FastAPI()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://ieee_user:ieee_password@localhost:5432/ieee_app",
)


@app.get("/")
def home():
    return {"message": "Hello IEEE DevOps Project!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-health")
def database_health():
    try:
        with psycopg.connect(DATABASE_URL) as connection:
            return {"database": "ok"}
    except Exception:
        return {"database": "error"}