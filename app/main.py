from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(title="Cloud API - FastAPI", version="1.0.0")

# Modelo para validar POST
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=60)
    age: int = Field(..., ge=0, le=120)
    email: EmailStr

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "app": "Cloud API - FastAPI",
        "version": "1.0.0",
        "author": "Sebastián Proaño"
    }

@app.post("/users")
def create_user(user: UserCreate):
    # Respuesta JSON (FastAPI lo hace automático)
    return {
        "created": True,
        "user": user.model_dump()
    }