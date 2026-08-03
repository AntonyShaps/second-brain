from uuid import uuid4

from fastapi import APIRouter, status

from app.entries.schemas import EntryCreate, EntryRead

router = APIRouter(
        prefix="/entries",
        tags=["entries"],
        )

@router.post(
        "",
        response_model=EntryRead,
        status_code=status.HTTP_201_CREATED,
        )
def create_entry(entry: EntryCreate) -> EntryRead:
    return EntryRead(
            id=uuid4(),
            **entry.model_dump(),
            )

