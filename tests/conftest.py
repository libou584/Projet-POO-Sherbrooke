import pytest
import sqlite3
import os

from models.Users.Employee import Employee
from models.Repositories.RepositoryFacade import RepositoryFacade
from app import app


@pytest.fixture
def mock_user():
    return Employee(0, 'John', 'Doe', 25)


@pytest.fixture
def mock_repository_facade():
    yield RepositoryFacade(db_name="test_database.db")
    # Cleanup
    if os.path.exists("test_database.db"):
        os.remove("test_database.db")


@pytest.fixture
def client():
    with app.test_client() as client:
        return client