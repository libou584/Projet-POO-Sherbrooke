from models.Repositories.UserRepository import UserRepository
from models.Repositories.DaysOffRepository import DaysOffRepository
from models.Repositories.NotificationRepository import NotificationRepository


class RepositoryFacade:

    def __init__(self, db_name="database.db"):
        self.__user_repository = UserRepository(db_name)
        self.__days_off_repository = DaysOffRepository(db_name)
        self.__notification_repository = NotificationRepository(db_name)
    
    def clear_tables(self):
        self.__user_repository.clear_table()
        self.__days_off_repository.clear_table()
        self.__notification_repository.clear_table()
    
    def new_employee(self, first_name: str, last_name: str, age: int):
        return self.__user_repository.new_employee(first_name, last_name, age)
    
    def new_hr(self, first_name: str, last_name: str, age: int):
        return self.__user_repository.new_hr(first_name, last_name, age)
    
    def get_user_by_id(self, id: int):
        return self.__user_repository.get_by_id(id)
    
    def get_all_users(self):
        return self.__user_repository.get_all_users()
    
    def get_all_employees(self):
        return self.__user_repository.get_all_employees()

    def add_booked_day(self, id: int, date: str) -> bool:
        return self.__days_off_repository.add_booked_day(id, date)
    
    def get_booked_days_by_employee_id(self, id: int):
        return self.__days_off_repository.get_booked_days_by_employee_id(id)

    def get_booked_days_by_hr_id(self, id: int):
        return self.__days_off_repository.get_booked_days_by_hr_id(id)
    
    def get_all_booked_days(self):
        return self.__days_off_repository.get_all_booked_days()
    
    def approve_day_off(self, id: int, date: str, hr_id: int):
        self.__days_off_repository.approve_day_off(id, date, hr_id)

    def reject_day_off(self, id: int, date: str, hr_id: int):
        self.__days_off_repository.reject_day_off(id, date, hr_id)
    
    def send_employee_notification(self, user_id: int, message: str):
        self.__notification_repository.send_employee_notification(user_id, message)
    
    def send_hr_notification(self, message: str):
        self.__notification_repository.send_hr_notification(message)
    
    def get_all_notifications(self):
        return self.__notification_repository.get_all_notifications()
    
    def get_notifications_by_user_id(self, user_id: int):
        return self.__notification_repository.get_notifications_by_user_id(user_id)