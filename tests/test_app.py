import sys
import pytest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from server.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test pour l'endpoint /villes
def test_villes(client):
    response = client.get('/villes')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test pour l'endpoint /quartiers/<ville>
def test_quartiers(client):
    ville_test = "Berlin"
    response = client.get(f'/quartiers/{ville_test}')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test pour l'endpoint /prix/<quartier>/<ville>
def test_prix(client):
    ville_test = "Berlin"
    quartier_test = "Centre"
    response = client.get(f'/prix/{quartier_test}/{ville_test}')
    assert response.status_code == 200
    assert "prix" in response.json
    assert isinstance(response.json['prix'], list)
