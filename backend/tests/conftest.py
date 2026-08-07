import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base, get_session
from app.main import app

@pytest.fixture
def client(tmp_path):
    database_path = tmp_path / "test.db"

    test_engine = create_engine(
            f"sqlite:///{database_path}",
            connect_args={"check_same_thread":False},
            )

    TestSessionLocal = sessionmaker(
            bind=test_engine,
            autoflush=False,
            expire_on_commit=False,
            )
    Base.metadata.create_all(bind=test_engine)
    def override_get_session():
        with TestSessionLocal() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    test_engine.dispose()
