"""End-to-end API tests exercising the FastAPI app with a real test client."""
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health_check():
    """GET /api/health should report the API as running."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_generate_password_default_options():
    """POST /api/generate should return a password matching the requested length."""
    response = client.post("/api/generate", json={"length": 16})
    assert response.status_code == 200

    body = response.json()
    assert len(body["password"]) == 16
    assert body["strength"] in {"Weak", "Medium", "Strong"}
    assert 0 <= body["score"] <= 100
    assert body["id"] > 0


def test_generate_password_rejects_invalid_options():
    """Disabling every character set should surface the legacy validation error."""
    response = client.post(
        "/api/generate",
        json={
            "length": 12,
            "use_uppercase": False,
            "use_lowercase": False,
            "use_numbers": False,
            "use_symbols": False,
        },
    )
    assert response.status_code == 422
    assert "character type" in response.json()["detail"]


def test_strength_endpoint_scores_a_password():
    """POST /api/strength should report entropy and a strength label."""
    response = client.post("/api/strength", json={"password": "Correct-Horse-Battery-42"})
    assert response.status_code == 200

    body = response.json()
    assert body["password_length"] == len("Correct-Horse-Battery-42")
    assert body["strength"] in {"Weak", "Medium", "Strong"}


def test_history_lifecycle():
    """Generated passwords should appear in history and be clearable."""
    client.post("/api/generate", json={"length": 10})

    history_response = client.get("/api/history")
    assert history_response.status_code == 200
    assert len(history_response.json()) >= 1

    delete_response = client.delete("/api/history")
    assert delete_response.status_code == 200
    assert delete_response.json()["deleted"] >= 1

    empty_history = client.get("/api/history")
    assert empty_history.json() == []


def test_export_endpoints_return_files():
    """Export endpoints should return downloadable txt/csv files after generation."""
    client.post("/api/generate", json={"length": 14})

    txt_response = client.get("/api/export/txt")
    assert txt_response.status_code == 200
    assert txt_response.headers["content-type"].startswith("text/plain")

    csv_response = client.get("/api/export/csv")
    assert csv_response.status_code == 200
    assert csv_response.headers["content-type"].startswith("text/csv")
