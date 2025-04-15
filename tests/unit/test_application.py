import pytest
from models.Application import Application
from models.DayOffApproval.HRToApproveStrategy import HRToApproveStategy
from models.Users.Employee import Employee


def test_application_instance():
    app1 = Application()
    app2 = Application()
    assert app1 == app2
    assert app1 is app2


def test_login(mock_user):
    app = Application()
    assert app.user is None
    app.login(mock_user)
    assert app.user.__str__() == 'John Doe'

def test_logout(mock_user):
    app = Application()
    app.login(mock_user)
    app.logout()
    assert app.user is None

def test_strategy():
    application = Application()
    application.day_off_approval_strategy = HRToApproveStategy()
    assert isinstance(application.day_off_approval_strategy, HRToApproveStategy)