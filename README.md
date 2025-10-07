# FastAPI sample project

This is a minimal FastAPI project that exposes Swagger UI automatically at /docs and ReDoc at /redoc.

How to run (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open: http://127.0.0.1:8000/docs
