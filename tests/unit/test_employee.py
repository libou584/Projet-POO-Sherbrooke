from models.Employee import Employee


def test_employee_instance():
    employee = Employee(0, 'John', 'Doe', 25)
    assert employee.id == 0
    assert employee.first_name == 'John'
    assert employee.last_name == 'Doe'
    assert employee.age == 25
    assert employee.booked_days == []
    assert employee.__str__() == 'John Doe'


def test_book_day():
    employee = Employee(0, 'John', 'Doe', 25)
    employee.book_day('2020-01-03')
    assert employee.booked_days == ['2020-01-03']
    employee.book_day('2020-01-02')
    assert employee.booked_days == ['2020-01-02', '2020-01-03']
    employee.book_day('2020-01-01')
    assert employee.booked_days == ['2020-01-01', '2020-01-02', '2020-01-03']
    employee.book_day('2020-01-02')
    assert employee.booked_days == ['2020-01-01', '2020-01-02', '2020-01-03']