from fastapi import FastAPI
from .routers import players, events
from contextlib import asynccontextmanager
from .db.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startataan")
    create_db()
    yield
    print("Lopetellaan")

app = FastAPI(lifespan = lifespan)

app.include_router(players.router)
app.include_router(events.router)