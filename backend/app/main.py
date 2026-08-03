from fastapi import FastAPI

from app.entries.router import router as entries_router


app = FastAPI(title="Second Brain API")

app.include_router(entries_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "heee"}
