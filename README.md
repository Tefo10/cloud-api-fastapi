# Cloud API - FastAPI

API mínima en FastAPI con:
- GET /health
- POST /users (con validación)

## Requisitos
- Python 3.10+ (recomendado 3.11)

## Ejecutar local
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080