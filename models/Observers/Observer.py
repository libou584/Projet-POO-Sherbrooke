from abc import ABC


class Observer(ABC):

    def update(self, notification_type: str, user_id: int, message: str):
        """
        Update the observer with the notification type, user ID, and message.
        user_id is -1 if the type is hr.
        """
        pass