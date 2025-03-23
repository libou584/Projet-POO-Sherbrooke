import pytest
from models.Application import Application


def test_application_instance():
    app1 = Application()
    app2 = Application()
    assert app1 == app2
    assert app1 is app2