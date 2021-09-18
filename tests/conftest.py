import pytest

from app import create_app, db

@pytest.fixture
def app(): return create_app(True)

@pytest.fixture
def database(app):
    db.create_all()
    return db
