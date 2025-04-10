from models.Users.Hr import Hr
from models.Users.Employee import Employee
from models.Application import Application


def test_approve_booked_days(mock_repository_facade):
    mock_repository_facade.clear_tables()
    application = Application()
    application.repository_facade = mock_repository_facade
    application.repository_facade.new_employee('John', 'Doe', 25)
    application.repository_facade.new_hr('Jane', 'Smith', 30)
    hr = application.repository_facade.get_user_by_id(1)
    application.repository_facade.add_booked_day(0, '2020-01-03')
    application.repository_facade.approve_day_off(0, '2020-01-03', 1)
    hr.refresh()

    assert application.repository_facade.get_booked_days_by_hr_id(1) == [(0, '2020-01-03', 'approved')]

    assert hr.approved_booked_days == [(0, '2020-01-03', 'approved')]