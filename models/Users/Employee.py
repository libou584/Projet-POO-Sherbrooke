from models.Users.User import User


class Employee(User):

    def __init__(self, id: int, first_name: str, last_name: str, age: int):
        super().__init__(id, first_name, last_name, age)
        self.__get_booked_days_from_database()
    
    def refresh(self):
        self.__get_booked_days_from_database()

    @property
    def booked_days(self):
        return self.__booked_days
    
    def __get_booked_days_from_database(self):
        from models.Application import Application
        application = Application()
        self.__booked_days = application.repository_facade.get_booked_days_by_employee_id(self.id)