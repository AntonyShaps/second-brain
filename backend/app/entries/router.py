from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_session
from app.entries.models import EntryModel
from app.entries.schemas import EntryCreate, EntryRead

router = APIRouter(
        prefix="/entries",
        tags=["entries"],
        )

SessionDependency = Annotated[Session, Depends(get_session)]


@router.post(
        "",
        response_model=EntryRead,
        status_code=status.HTTP_201_CREATED,
        )
def create_entry(entry: EntryCreate, session: SessionDependency) -> EntryModel:
    db_entry = EntryModel(
            type=entry.type.value,
            title=entry.title,
            contents=entry.contents,
            tags=entry.tags,
            )
    session.add(db_entry)
    session.commit()
    session.refresh(db_entry)

    return db_entry

@router.get(
        "",
        response_model=list[EntryRead],
        )
def list_entries(
        session: SessionDependency,
        ) -> list[EntryModel]:
    statement = select(EntryModel)
    entries = session.scalars(statement).all()

    return list(entries)

