from models.Users.User import User


class Hr(User):

    def __init__(self, id: int, first_name: str, last_name: str, age: int):
        super().__init__(id, first_name, last_name, age)