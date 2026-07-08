from fastapi import FastAPI
from database import engine, Base
from auth import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="JWT Authentication API"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "JWT Authentication Demo"
    }
