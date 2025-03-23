from abc import ABC as AbstractClass


class User(AbstractClass):

    def __init__(self, id: int, first_name: str, last_name: str, email: str):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} <{self.__email}>"

    @property
    def id(self):
        return self.__id
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def email(self):
        return self.__email