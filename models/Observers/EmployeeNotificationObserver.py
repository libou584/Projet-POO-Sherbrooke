from models.Observers.Observer import Observer
from models.Application import Application


class EmployeeNotificationObserver(Observer):
    """
    Observer for the employee notification system.
    """

    def __init__(self, application: Application):
        application.register_observer(self)

    def update(self, notification_type: str, user_id: int, message: str):
        if notification_type == "employee":
            self.__send_notification(user_id, message)
    
    def __send_notification(self, user_id: int, message: str):
        application = Application()
        application.repository_facade.send_employee_notification(user_id, message)