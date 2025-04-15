from models.Application import Application
from models.Observers.Observer import Observer
from models.Observers.EmployeeNotificationObserver import EmployeeNotificationObserver
from models.Observers.HrNotificationObserver import HrNotificationObserver


def test_register_observer():
    application = Application()
    observer = Observer()
    application.register_observer(observer)
    assert observer in application.observers

def test_remove_observer():
    application = Application()
    observer = Observer()
    application.register_observer(observer)
    application.remove_observer(observer)
    assert observer not in application.observers

def test_notify_observers(mock_repository_facade):
    mock_repository_facade.clear_tables()
    application = Application()
    while len(application.observers) > 0:
        application.remove_observer(application.observers[0])
    application.repository_facade = mock_repository_facade
    EmployeeNotificationObserver(application)
    application.notify_observers("employee", 1, "test")
    print(application.observers)
    assert len(application.repository_facade.get_notifications_by_user_id(1)) == 1