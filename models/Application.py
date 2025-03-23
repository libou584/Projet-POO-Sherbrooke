class Application:
    __instance = None

    def __new_app(self):
        self.__user_logged_in = None
        self.__database_handler = None
        self.__booked_days: list[str] = []

    def __new__(cls):
        if cls.__instance is None:
            instance = super().__new__(cls)
            instance.__new_app()
            cls.__instance = instance
        return cls.__instance
    
    @property
    def booked_days(self):
        return self.__booked_days
    
    def book_day(self, date: str):
        if date not in self.__booked_days:
            self.__booked_days.append(date)
            self.sort_dates()
    
    def sort_dates(self):
        self.__booked_days.sort(key=lambda x: tuple(map(int, x.split('-'))))