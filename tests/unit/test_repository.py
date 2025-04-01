from models.Employee import Employee
import pytest


def test_new_employee(mock_repository):
    mock_repository.new_employee("John", "Doe", 30)
    users = mock_repository.get_all_users()
    
    assert len(users) == 1
    assert isinstance(users[0], Employee)
    assert users[0].first_name == "John"
    assert users[0].last_name == "Doe"
    assert users[0].age == 30

def test_get_all_users_empty(mock_repository):
    users = mock_repository.get_all_users()
    assert len(users) == 0

def test_get_all_users_multiple(mock_repository):
    mock_repository.new_employee("John", "Doe", 30)
    mock_repository.new_employee("Jane", "Smith", 25)
    
    users = mock_repository.get_all_users()
    assert len(users) == 2
    assert all(isinstance(user, Employee) for user in users)

def test_get_user_by_id(mock_repository):
    mock_repository.new_employee("John", "Doe", 30)
    user = mock_repository.get_user_by_id(0)  # First user should have id 0
    
    assert isinstance(user, Employee)
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.age == 30

def test_get_user_by_id_not_found(mock_repository):
    user = mock_repository.get_user_by_id(999)  # Non-existent ID
    assert user is None

def test_sequential_id_assignment(mock_repository):
    mock_repository.new_employee("John", "Doe", 30)
    mock_repository.new_employee("Jane", "Smith", 25)
    
    users = mock_repository.get_all_users()
    assert users[0].id == 0
    assert users[1].id == 1