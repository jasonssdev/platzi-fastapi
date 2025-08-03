import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_client_creation(client):
    """Test that the client is properly created."""
    assert isinstance(client, TestClient)


def test_root_endpoint(client):
    """Test the root endpoint returns the expected message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_time_endpoint(client):
    """Test the time endpoint returns current time."""
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert "current_time" in data
    assert isinstance(data["current_time"], str)
