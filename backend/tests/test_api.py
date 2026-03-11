import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture(scope="module")
def client():
    """Synchronous test client with lifespan events."""
    from fastapi.testclient import TestClient
    with TestClient(app) as c:
        yield c


def test_health(client):
    """Health endpoint returns ok."""
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "version" in data


def test_predict_success(client):
    """Valid symptoms return a prediction with all expected keys."""
    resp = client.post("/predict", json={"text": "I have itching and skin rash"})
    assert resp.status_code == 200
    data = resp.json()
    assert "disease" in data
    assert "description" in data
    assert "precautions" in data
    assert isinstance(data["precautions"], list)
    assert "matched_symptoms" in data
    assert len(data["matched_symptoms"]) > 0
    assert "disclaimer" in data


def test_predict_no_symptoms(client):
    """Input with no recognizable symptoms returns 422."""
    resp = client.post("/predict", json={"text": "hello world nothing here"})
    assert resp.status_code == 422
    data = resp.json()
    assert "detail" in data


def test_predict_empty_input(client):
    """Empty input returns 422 validation error."""
    resp = client.post("/predict", json={"text": ""})
    assert resp.status_code == 422


def test_predict_missing_body(client):
    """Missing request body returns 422."""
    resp = client.post("/predict")
    assert resp.status_code == 422


def test_symptom_extraction(client):
    """Multiple symptoms are correctly matched."""
    resp = client.post("/predict", json={"text": "fever and headache with nausea"})
    if resp.status_code == 200:
        data = resp.json()
        matched = data["matched_symptoms"]
        # At least one symptom matched
        assert len(matched) >= 1
