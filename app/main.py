from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="FastAPI Boilerplate")

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "FastAPI Boilerplate Running"}
