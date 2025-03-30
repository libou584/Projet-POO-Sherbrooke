import pytest

from models.Employee import Employee


@pytest.fixture
def mock_user():
    return Employee(0, 'John', 'Doe', 25)