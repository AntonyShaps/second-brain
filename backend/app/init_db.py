from app.database import Base, engine
from app.entries.models import EntryModel

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
