from models.Employee import Employee
from models.Application import Application


def test_employee_instance(mock_repository):
    employee = Employee(0, 'John', 'Doe', 25)
    application = Application()
    application.repository = mock_repository
    assert employee.id == 0
    assert employee.first_name == 'John'
    assert employee.last_name == 'Doe'
    assert employee.age == 25
    assert isinstance(employee.booked_days, list)
    assert employee.__str__() == 'John Doe'


def test_book_day(mock_repository):
    application = Application()
    application.repository = mock_repository
    application.repository.new_employee('John', 'Doe', 25)
    employee = application.repository.get_user_by_id(0)
    application.repository.add_booked_day(0, '2020-01-03')
    employee.refresh()
    assert employee.booked_days == [('2020-01-03', 'waiting')]
    application.repository.add_booked_day(0, '2020-01-02')
    employee.refresh()
    assert employee.booked_days == [('2020-01-02', 'waiting'), ('2020-01-03', 'waiting')]
    application.repository.add_booked_day(0, '2020-01-01')
    employee.refresh()
    assert employee.booked_days == [('2020-01-01', 'waiting'), ('2020-01-02', 'waiting'), ('2020-01-03', 'waiting')]
    application.repository.add_booked_day(0, '2020-01-02')
    employee.refresh()
    assert employee.booked_days == [('2020-01-01', 'waiting'), ('2020-01-02', 'waiting'), ('2020-01-03', 'waiting')]