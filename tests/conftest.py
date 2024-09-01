import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.templates_api.main import app
from src.templates_api.database import Base, get_db

SQLALQUEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALQUEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# Fixture to pre-populate the database with some items
# @pytest.fixture(scope="function")
# def test_db(db):
#     # Create test data
#     test_item = Item(
#         name="Test Item", description="This is a test item", price=100.0, quantity=10
#     )
#     db.add(test_item)
#     db.commit()
#     return db
