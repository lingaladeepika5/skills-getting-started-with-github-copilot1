import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test activities list endpoint
def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test signup endpoint
def test_signup_activity():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    response = client.post(f"/api/activities/{activity}/signup", json={"email": email})
    assert response.status_code == 200 or response.status_code == 400

# Test unregister endpoint
def test_unregister_activity():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@example.com"
    # First, ensure user is signed up
    client.post(f"/api/activities/{activity}/signup", json={"email": email})
    # Now, unregister
    response = client.post(f"/api/activities/{activity}/unregister", json={"email": email})
    assert response.status_code == 200 or response.status_code == 400
