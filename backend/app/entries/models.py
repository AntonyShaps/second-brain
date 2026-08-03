from uuid import UUID, uuid4

from sqlalchemy import JSON, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class EntryModel(Base):
    __tablename__ = "entries"

    id: Mapped[UUID] = mapped_column(
            Uuid,
            primary_key=True,
            default=uuid4,
            )
    type: Mapped[str] = mapped_column(
            String(30),
            nullable=False,
            )
    title: Mapped[str] = mapped_column(
            String(200),
            nullable=False,
            )
    contents: Mapped[str | None] = mapped_column(
            Text,
            nullable=True,
            )
    tags: Mapped[list[str]] = mapped_column(
            JSON,
            nullable=False,
            default=list,
            )
