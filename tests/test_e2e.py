import pytest
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_websocket_compute():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({"operation": "add", "a": 5, "b": 3})
        data = websocket.receive_json()
        assert data["operation"] == "add"
        assert data["result"] == 8

def test_websocket_invalid_op():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({"operation": "invalid", "a": 5, "b": 3})
        data = websocket.receive_json()
        assert "error" in data
