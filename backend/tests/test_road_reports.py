from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_road_report_requires_authentication():
    response = client.post(
        "/api/v1/road-reports/",
        json={
            "latitude": 16.5062,
            "longitude": 80.6480,
            "damage_type": "Pothole",
            "severity": "High",
            "image_path": "uploads/test_pothole.jpg"
        }
    )

    assert response.status_code == 401