from fastapi import FastAPI

from app.database import Base, engine
from app.entries.models import EntryModel

from app.entries.router import router as entries_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Second Brain API")

app.include_router(entries_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "heee"}
