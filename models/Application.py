class Application:

    __instance = None

    def __new_app(self):
        self.__logged_in_user = None
        self.__database_handler = None

    def __new__(cls):
        if cls.__instance is None:
            instance = super().__new__(cls)
            instance.__new_app()
            cls.__instance = instance
        return cls.__instance
    
    @property
    def user(self):
        return self.__logged_in_user
    
    def login(self, user):
        self.__logged_in_user = user