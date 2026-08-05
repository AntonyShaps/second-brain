from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.entries.models import EntryModel

from app.entries.router import router as entries_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Second Brain API")

app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            ],
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
        allow_headers=["*"],
        )

app.include_router(entries_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "heee"}
