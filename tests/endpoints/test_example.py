from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_get_example():
    response = client.get('/api/v1/example')
    assert response.status_code == 200
    assert response.json() == {'message': 'hello'}
