from models.Repositories.RepositoryFacade import RepositoryFacade
from models.DayOffApproval.HRToApproveStrategy import HRToApproveStategy


class Application:

    __instance = None

    def __new_app(self):
        self.__logged_in_user = None
        self.__repository_facade = RepositoryFacade()
        self.__day_off_approval_strategy = HRToApproveStategy()

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
    def repository_facade(self):
        return self.__repository_facade
    
    @property
    def day_off_approval_strategy(self):
        return self.__day_off_approval_strategy
    
    @repository_facade.setter
    def repository_facade(self, repository_facade):
        self.__repository_facade = repository_facade

    @day_off_approval_strategy.setter
    def day_off_approval_strategy(self, strategy):
        self.__day_off_approval_strategy = strategy
    
    def login(self, user):
        self.__logged_in_user = user

    def logout(self):
        self.__logged_in_user = None