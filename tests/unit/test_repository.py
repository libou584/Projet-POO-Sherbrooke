from models.Employee import Employee
import pytest


def test_new_employee(repository):
    repository.new_employee("John", "Doe", 30)
    users = repository.get_all_users()
    
    assert len(users) == 1
    assert isinstance(users[0], Employee)
    assert users[0].first_name == "John"
    assert users[0].last_name == "Doe"
    assert users[0].age == 30

def test_get_all_users_empty(repository):
    users = repository.get_all_users()
    assert len(users) == 0

def test_get_all_users_multiple(repository):
    repository.new_employee("John", "Doe", 30)
    repository.new_employee("Jane", "Smith", 25)
    
    users = repository.get_all_users()
    assert len(users) == 2
    assert all(isinstance(user, Employee) for user in users)

def test_get_user_by_id(repository):
    repository.new_employee("John", "Doe", 30)
    user = repository.get_user_by_id(0)  # First user should have id 0
    
    assert isinstance(user, Employee)
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.age == 30

def test_get_user_by_id_not_found(repository):
    user = repository.get_user_by_id(999)  # Non-existent ID
    assert user is None

def test_sequential_id_assignment(repository):
    repository.new_employee("John", "Doe", 30)
    repository.new_employee("Jane", "Smith", 25)
    
    users = repository.get_all_users()
    assert users[0].id == 0
    assert users[1].id == 1