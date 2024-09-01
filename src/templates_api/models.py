from sqlalchemy import Column, Float, Integer, String

from .database import Base


class Item(Base):
    __tablename__ = "items"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
