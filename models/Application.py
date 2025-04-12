from models.Repositories.RepositoryFacade import RepositoryFacade
from models.DayOffApproval.HRToApproveStrategy import HRToApproveStategy


class Application:

    __instance = None

    def __new_app(self):
        self.__logged_in_user = None
        self.__repository_facade = RepositoryFacade()
        self.__day_off_approval_strategy = HRToApproveStategy()
        self.__observers = []

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
    
    @property
    def observers(self):
        return self.__observers
    
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
    
    def register_observer(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.remove(observer)
    
    def notify_observers(self, notification_type: str, user_id: int, message: str):
        for observer in self.__observers:
            observer.update(notification_type, user_id, message)