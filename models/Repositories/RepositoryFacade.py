from models.Repositories.UserRepository import UserRepository
from models.Repositories.DaysOffRepository import DaysOffRepository


class RepositoryFacade:

    def __init__(self, db_name="database.db"):
        self.__user_repository = UserRepository(db_name)
        self.__days_off_repository = DaysOffRepository(db_name)
    
    def clear_tables(self):
        self.__user_repository.clear_table()
        self.__days_off_repository.clear_table()
    
    def new_employee(self, first_name: str, last_name: str, age: int):
        return self.__user_repository.new_employee(first_name, last_name, age)
    
    def new_hr(self, first_name: str, last_name: str, age: int):
        return self.__user_repository.new_hr(first_name, last_name, age)
    
    def get_user_by_id(self, id: int):
        return self.__user_repository.get_by_id(id)
    
    def get_all_users(self):
        return self.__user_repository.get_all_users()

    def add_booked_day(self, id: int, date: str) -> bool:
        return self.__days_off_repository.add_booked_day(id, date)
    
    def get_booked_days(self, id: int):
        return self.__days_off_repository.get_booked_days(id)
    
    def get_all_booked_days(self):
        return self.__days_off_repository.get_all_booked_days()
    
    def approve_day_off(self, id: int, date: str):
        self.__days_off_repository.approve_day_off(id, date)

    def reject_day_off(self, id: int, date: str):
        self.__days_off_repository.reject_day_off(id, date)