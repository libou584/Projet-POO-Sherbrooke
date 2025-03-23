import pytest
from models.Application import Application


def test_application_instance():
    app1 = Application()
    app2 = Application()
    assert app1 == app2
    assert app1 is app2


def test_book_day():
    app = Application()
    app.book_day('2021-01-04')
    assert app.booked_days == ['2021-01-04']
    app.book_day('2021-01-05')
    assert app.booked_days == ['2021-01-04', '2021-01-05']
    app.book_day('2021-01-04')
    assert app.booked_days == ['2021-01-04', '2021-01-05']
    app.book_day('2021-01-03')
    assert app.booked_days == ['2021-01-03', '2021-01-04', '2021-01-05']
