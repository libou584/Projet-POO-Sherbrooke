from models.Repository import Repository


class Application:

    __instance = None

    def __new_app(self):
        self.__logged_in_user = None
        self.__repository = Repository()

    def __new__(cls):
        if cls.__instance is None:
            instance = super().__new__(cls)
            instance.__new_app()
            cls.__instance = instance
        return cls.__instance
    
    @property
    def user(self):
        return self.__logged_in_user
    
    @property
    def repository(self):
        return self.__repository
    
    @repository.setter
    def repository(self, repository):
        self.__repository = repository
    
    def login(self, user):
        self.__logged_in_user = user

    def logout(self):
        self.__logged_in_user = None