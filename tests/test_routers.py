from fastapi.testclient import TestClient
from src.templates_api.main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/api/v1/items/",
        json={
            "name": "Test Item",
            "description": "This is a test item",
            "price": 100.0,
            "quantity": 10,
        },
    )
    assert response.status_code == 201
    created_item = response.json()
    assert created_item["name"] == "Test Item"
    assert created_item["description"] == "This is a test item"
    assert created_item["price"] == 100.0
    assert created_item["quantity"] == 10
    assert created_item["id"] is not None


def test_read_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_item():
    response = client.post(
        "/api/v1/items/",
        json={
            "name": "Test Item",
            "description": "This is a test item",
            "price": 100.0,
            "quantity": 10,
        },
    )
    created_item = response.json()
    item_id = created_item["id"]

    response = client.get(f"/api/v1/items/{item_id}")
    fetched_item = response.json()
    assert response.status_code == 200
    assert fetched_item == created_item


def test_update_item():
    response = client.post(
        "/api/v1/items/",
        json={
            "name": "Test Item",
            "description": "This is a test item",
            "price": 100.0,
            "quantity": 10,
        },
    )
    created_item = response.json()
    item_id = created_item["id"]

    response = client.put(
        f"/api/v1/items/{item_id}",
        json={"name": "Updated Test Item", "price": 10.0},
    )
    updated_item = response.json()
    assert response.status_code == 200
    assert updated_item["name"] == "Updated Test Item"
    assert updated_item["price"] == 10.0
    assert updated_item["description"] == created_item["description"]
    assert updated_item["quantity"] == created_item["quantity"]


def test_delete_item():
    response = client.post(
        "/api/v1/items/",
        json={
            "name": "Test Item",
            "description": "This is a test item",
            "price": 100.0,
            "quantity": 10,
        },
    )
    created_item = response.json()
    item_id = created_item["id"]

    response = client.delete(f"/api/v1/items/{item_id}")
    deleted_item = response.json()
    assert response.status_code == 200
    assert deleted_item == created_item

    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 404
