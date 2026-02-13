from fastapi import FastAPI
from app.routers import health, users

app = FastAPI(title="FastAPI Boilerplate")

app.include_router(health.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI Boilerplate Running"}
