from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/")
def root():
    return {
        "message": "Welcome to YC64 ERP API",
        "debug": settings.debug,
        "database": settings.database_url,
    }