from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.ask import router as ask_router

app = FastAPI(title="Booking AI")

app.include_router(ask_router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")