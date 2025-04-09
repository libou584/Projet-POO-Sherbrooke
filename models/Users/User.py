from abc import ABC as AbstractClass


class User(AbstractClass):

    def __init__(self, id: int, first_name: str, last_name: str, age: int):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}"

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
    def age(self):
        return self.__age