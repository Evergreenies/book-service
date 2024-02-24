import pytest
from sqlalchemy.orm import sessionmaker
from pytest_alembic.config import Config

from twelve_factor_app import app
from tests.test_databse_setup import database_url, engine_maker


@pytest.fixture
def test_app():
    book_app = app.app
    with book_app.app_context():
        book_app.config["SQLALCHEMY_DATABASE_URI"] = database_url
        print(f"DBURL ===> {database_url}")
        yield book_app


@pytest.fixture
def alembic_engine():
    return sessionmaker(bind=engine_maker())


@pytest.fixture
def alembic_config():
    return Config()


@pytest.fixture
def client():
    return app.app.test_client()
