from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_get_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json() == {'message': 'service is healthy'}
