from models.Users.Employee import Employee
from models.Users.Hr import Hr
from models.Application import Application
import pytest


def test_new_employee(mock_repository_facade):
    mock_repository_facade.new_employee("John", "Doe", 30)
    users = mock_repository_facade.get_all_users()
    
    assert len(users) == 1
    assert isinstance(users[0], Employee)
    assert users[0].first_name == "John"
    assert users[0].last_name == "Doe"
    assert users[0].age == 30

def test_new_hr(mock_repository_facade):
    mock_repository_facade.new_hr("Jane", "Smith", 25)
    users = mock_repository_facade.get_all_users()
    
    assert len(users) == 1
    assert isinstance(users[0], Hr)
    assert users[0].first_name == "Jane"
    assert users[0].last_name == "Smith"
    assert users[0].age == 25

def test_get_all_users_empty(mock_repository_facade):
    users = mock_repository_facade.get_all_users()
    assert len(users) == 0

def test_get_all_users_multiple(mock_repository_facade):
    mock_repository_facade.new_employee("John", "Doe", 30)
    mock_repository_facade.new_hr("Jane", "Smith", 25)
    
    users = mock_repository_facade.get_all_users()
    assert len(users) == 2
    assert all(isinstance(user, Employee) or isinstance(user, Hr) for user in users)

def test_get_user_by_id(mock_repository_facade):
    user_id = mock_repository_facade.new_employee("John", "Doe", 30)
    user = mock_repository_facade.get_user_by_id(user_id)
    
    assert isinstance(user, Employee)
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.age == 30

    user_id = mock_repository_facade.new_hr("Jane", "Smith", 30)
    user = mock_repository_facade.get_user_by_id(user_id)
    
    assert isinstance(user, Hr)
    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.age == 30

def test_get_user_by_id_not_found(mock_repository_facade):
    user = mock_repository_facade.get_user_by_id(999)  # Non-existent ID
    assert user is None

def test_sequential_id_assignment(mock_repository_facade):
    mock_repository_facade.new_employee("John", "Doe", 30)
    mock_repository_facade.new_employee("Jane", "Smith", 25)
    
    users = mock_repository_facade.get_all_users()
    assert users[0].id == 0
    assert users[1].id == 1

def test_approve_reject_day_off(mock_repository_facade):
    application = Application()
    application.repository_facade = mock_repository_facade

    user_id = application.repository_facade.new_employee("Jon", "Doe", 30)
    employee = application.repository_facade.get_user_by_id(user_id)
    
    # Approve the day off
    application.repository_facade.add_booked_day(employee.id, '2023-10-01')
    employee.refresh()
    
    assert len(employee.booked_days) == 1
    assert employee.booked_days[0][1] == "waiting"

    application.repository_facade.approve_day_off(employee.id, '2023-10-01')
    employee.refresh()
    
    assert employee.booked_days[0][1] == "approved"

    # Reject the day off
    application.repository_facade.add_booked_day(employee.id, '2023-10-02')
    employee.refresh()

    assert len(employee.booked_days) == 2
    assert employee.booked_days[1][1] == "waiting"

    application.repository_facade.reject_day_off(employee.id, '2023-10-02')
    employee.refresh()

    assert employee.booked_days[1][1] == "rejected"
    application.repository_facade.clear_tables()

def test_all_booked_days(mock_repository_facade):
    application = Application()
    application.repository_facade = mock_repository_facade

    user_id = application.repository_facade.new_employee("Jon", "Doe", 30)
    employee = application.repository_facade.get_user_by_id(user_id)
    
    application.repository_facade.add_booked_day(employee.id, '2023-10-01')
    application.repository_facade.add_booked_day(employee.id, '2023-10-02')
    application.repository_facade.add_booked_day(employee.id, '2023-10-03')

    all_booked_days = application.repository_facade.get_all_booked_days()
    assert len(all_booked_days) == 3
    assert all_booked_days[0][0] == employee.id