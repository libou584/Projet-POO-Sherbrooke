from models.Users.User import User


class Hr(User):

    def __init__(self, id: int, first_name: str, last_name: str, age: int):
        super().__init__(id, first_name, last_name, age)
        self.__get_approved_booked_days_from_database()
    
    def refresh(self):
        self.__get_approved_booked_days_from_database()
    
    @property
    def approved_booked_days(self):
        return self.__approved_booked_days
    
    def __get_approved_booked_days_from_database(self):
        from models.Application import Application
        application = Application()
        self.__approved_booked_days = application.repository_facade.get_booked_days_by_hr_id(self.id)