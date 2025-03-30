from models.User import User


class Employee(User):

    def __init__(self, id: int, first_name: str, last_name: str, age: int):
        super().__init__(id, first_name, last_name, age)
        self.__booked_days = []

    @property
    def booked_days(self):
        return self.__booked_days
    
    def book_day(self, date: str):
        if date not in self.__booked_days:
            self.__booked_days.append(date)
            self.sort_dates()
    
    def sort_dates(self):
        self.__booked_days.sort(key=lambda x: tuple(map(int, x.split('-'))))