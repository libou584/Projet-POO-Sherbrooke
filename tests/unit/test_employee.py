from models.Users.Employee import Employee
from models.Application import Application


def test_employee_instance(mock_repository_facade):
    mock_repository_facade.clear_tables()
    employee = Employee(0, 'John', 'Doe', 25)
    application = Application()
    application.repository_facade = mock_repository_facade
    assert employee.id == 0
    assert employee.first_name == 'John'
    assert employee.last_name == 'Doe'
    assert employee.age == 25
    assert isinstance(employee.booked_days, list)
    assert employee.__str__() == 'John Doe'


def test_book_day(mock_repository_facade):
    mock_repository_facade.clear_tables()
    application = Application()
    application.repository_facade = mock_repository_facade
    application.repository_facade.new_employee('John', 'Doe', 25)
    employee = application.repository_facade.get_user_by_id(0)
    application.repository_facade.add_booked_day(0, '2020-01-03')
    employee.refresh()
    assert employee.booked_days == [('2020-01-03', 'waiting', -1)]
    application.repository_facade.add_booked_day(0, '2020-01-02')
    employee.refresh()
    assert employee.booked_days == [('2020-01-02', 'waiting', -1), ('2020-01-03', 'waiting', -1)]
    application.repository_facade.add_booked_day(0, '2020-01-01')
    employee.refresh()
    assert employee.booked_days == [('2020-01-01', 'waiting', -1), ('2020-01-02', 'waiting', -1), ('2020-01-03', 'waiting', -1)]
    application.repository_facade.add_booked_day(0, '2020-01-02')
    employee.refresh()
    assert employee.booked_days == [('2020-01-01', 'waiting', -1), ('2020-01-02', 'waiting', -1), ('2020-01-03', 'waiting', -1)]
    application.repository_facade.clear_tables()