import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app', 'backend'))

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200


def test_health_returns_healthy(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_index_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_has_message(client):
    response = client.get('/')
    data = response.get_json()
    assert 'message' in data


def test_get_items_returns_200(client):
    response = client.get('/api/items')
    assert response.status_code == 200


def test_get_items_returns_list(client):
    response = client.get('/api/items')
    data = response.get_json()
    assert 'items' in data
    assert isinstance(data['items'], list)


def test_get_items_count(client):
    response = client.get('/api/items')
    data = response.get_json()
    assert data['count'] == len(data['items'])


def test_get_single_item(client):
    response = client.get('/api/items/1')
    assert response.status_code == 200


def test_get_single_item_has_name(client):
    response = client.get('/api/items/1')
    data = response.get_json()
    assert 'name' in data


def test_get_nonexistent_item(client):
    response = client.get('/api/items/999')
    assert response.status_code == 404