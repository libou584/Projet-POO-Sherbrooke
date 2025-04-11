from models.Observers.Observer import Observer
from models.Application import Application


class HrNotificationObserver(Observer):
    """
    Observer for the HR notification system.
    """

    def __init__(self, application: Application):
        application.register_observer(self)

    def update(self, notification_type: str, user_id: int, message: str):
        if notification_type == "hr":
            self.__send_notification(message)
    
    def __send_notification(self, message: str):
        application = Application()
        application.repository_facade.send_hr_notification(message)