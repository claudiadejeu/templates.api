from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Item, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    return crud.create_item(db=db, item=item)


@router.get("/", response_model=list[schemas.Item])
def read_items(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Maximum number of items to retrieve"),
    db: Session = Depends(get_db),
):
    """
    Retrieve a list of items.
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_class=schemas.Item)
def read_item(
    item_id: int = Path(..., title="The ID of the item to retrieve", ge=1),
    db: Session = Depends(get_db),
):
    """
    Retrieve an item by ID.
    """
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_class=schemas.Item)
def update_item(
    item_id: int = Path(..., title="The ID of the item to update", ge=1),
    item: schemas.ItemUpdate = Body(..., description="Updated item information"),
    db: Session = Depends(get_db),
):
    """
    Update an existing item by ID.
    """
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.patch("/{item_id}", response_class=schemas.Item)
def partial_update_item(
    item_id: int = Path(..., title="The ID of the item to update", ge=1),
    item: schemas.ItemUpdate = Body(..., description="Partial item updated information"),
    db: Session = Depends(get_db),
):
    """
    Partially update an existing item by ID.
    """
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}", response_class=schemas.Item)
def delete_item(
    item_id: int = Path(..., title="The ID of the item to delete", ge=1),
    db: Session = Depends(get_db),
):
    """
    Delete an item by ID.
    """
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/search/", response_class=List[schemas.Item])
def search_items(
    query: str = Query(..., description="Search query"),
    db: Session = Depends(get_db),
):
    """
    Search for items by query.
    """
    items = crud.search_items(db, query=query)
    return items
