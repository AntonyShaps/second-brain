from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_entry():
    response = client.post(
            "/api/v1/entries",
            json={
                "type": "note",
                "title": "first note",
                "contents": "heee",
                "tags": ["personal"],
                },
            )
    assert response.status_code == 201

    data = response.json()

    assert data["type"] == "note"
    assert data["title"] == "First note"
