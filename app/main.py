from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import auth

models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI(title="Minha API", version="1.0.0")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API a funcionar!"}