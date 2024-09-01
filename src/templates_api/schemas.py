from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    quantity: int | None = None


class Item(ItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
