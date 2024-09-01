from sqlalchemy.orm import Session
from src.templates_api import crud, schemas


def test_create_item(db: Session):
    item = schemas.ItemCreate(name="Test Name", description="This is a test item", price=100.0, quantity=10)
    created_item = crud.create_item(db, item)
    assert created_item.name == item.name
    assert created_item.description == item.description
    assert created_item.price == item.price
    assert created_item.quantity == item.quantity
    assert created_item.id is not None


def test_get_item(db: Session):
    item = schemas.ItemCreate(name="Test Name", description="This is a test item", price=100.0, quantity=10)
    created_item = crud.create_item(db, item)
    fetched_item = crud.get_item(db, created_item.id)
    assert created_item == fetched_item


def test_update_item(db: Session):
    item = schemas.ItemCreate(name="Test Name", description="This is a test item", price=100.0, quantity=10)
    created_item = crud.create_item(db, item)
    update_item = schemas.ItemUpdate(name="Updated Test Item", price=10.0)
    updated_item = crud.update_item(db, created_item.id, update_item)
    assert updated_item.name == update_item.name
    assert updated_item.price == update_item.price
    assert updated_item.description == created_item.description
    assert updated_item.quantity == created_item.quantity


def test_delete_item(db: Session):
    item = schemas.ItemCreate(name="Test Name", description="This is a test item", price=100.0, quantity=10)
    created_item = crud.create_item(db, item)
    deleted_item = crud.delete_item(db, created_item.id)
    assert deleted_item == created_item
    fetched_item = crud.get_item(db, created_item.id)
    assert fetched_item is None


def test_get_items(db: Session):
    items = [
        schemas.ItemCreate(name="Item 1", description="This is item 1", price=10.0, quantity=10),
        schemas.ItemCreate(name="Item 2", description="This is item 2", price=20.0, quantity=20),
        schemas.ItemCreate(name="Item 3", description="This is item 3", price=30.0, quantity=30),
    ]
    created_items = [crud.create_item(db, item) for item in items]
    fetched_items = crud.get_items(db)
    assert len(fetched_items) == len(created_items)
    for created_item, fetched_item in zip(created_items, fetched_items):
        assert created_item == fetched_item


def test_search_items(db: Session):
    items = [
        schemas.ItemCreate(name="Item 1", description="This is item 1", price=10.0, quantity=10),
        schemas.ItemCreate(name="Item 2", description="This is item 2", price=20.0, quantity=20),
        schemas.ItemCreate(name="Item 3", description="This is item 3", price=30.0, quantity=30),
    ]
    created_items = [crud.create_item(db, item) for item in items]
    searched_items = crud.search_items(db, "Item")
    assert len(searched_items) == len(created_items)
    for created_item, searched_item in zip(created_items, searched_items):
        assert created_item == searched_item
