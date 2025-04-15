from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

client = TestClient(app)


def test_create_meeting():
    response = client.post(
        "/meetings/",
        json={
            "title": "Test Meeting",
            "user_name": "John Doe",
            "email": "john.doe@example.com",
            "date": "2025-04-15",
            "time": "10:00:00",
        },
    )

    assert response.status_code == 201

    assert response.json()["meeting_id"]


def test_get_meeting():
    meeting_id = "some-id"
    response = client.get(f"/meetings/{meeting_id}")

    assert response.status_code == 201

    assert response.json()["id"] == meeting_id
    assert "title" in response.json()


def test_update_meeting():
    meeting_id = "some-id"
    response = client.put(
        f"/meetings/{meeting_id}", json={"title": "Updated Meeting", "confirmed": True}
    )

    assert response.status_code == 201

    assert response.json()["title"] == "Updated Meeting"
    assert response.json()["confirmed"] is True
