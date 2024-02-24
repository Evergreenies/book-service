import pytest

from twelve_factor_app import app
from tests.test_databse_setup import database_url


@pytest.fixture
def client():
    book_app = app.app
    with book_app.test_client() as client:
        book_app.config["SQLALCHEMY_DATABASE_URI"] = database_url
        yield client
