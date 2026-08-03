from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, Field

class EntryType(StrEnum):
    NOTE = "note"
    TASK = "task"
    PROJECT = "project"

class EntryCreate(BaseModel):
    type: EntryType
    title: str = Field(min_length=1, max_length=200)
    contents: str | None = None
    tags: list[str] = Field(default_factory=list)

class EntryRead(EntryCreate):
    id: UUID

