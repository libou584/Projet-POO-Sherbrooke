import pytest
from models.Application import Application


def test_application_instance():
    app1 = Application()
    app2 = Application()
    assert app1 == app2
    assert app1 is app2


def test_login(mock_user):
    app = Application()
    assert app.user is None
    app.login(mock_user)
    assert app.user.__str__() == 'John Doe <john.doe@udes.ca>'

def test_logout(mock_user):
    app = Application()
    app.login(mock_user)
    app.logout()
    assert app.user is None