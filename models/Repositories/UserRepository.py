from models.Repositories.BaseRepository import BaseRepository
from models.Users.Employee import Employee
from models.Users.Hr import Hr


class UserRepository(BaseRepository):

    def __init__(self, db_name="database.db"):
        super().__init__(db_name)
        self._initialize_table()
    
    def _initialize_table(self):
        self._cu.execute('''
            CREATE TABLE IF NOT EXISTS Users (id INT PRIMARY KEY, first_name TEXT, last_name TEXT, age INT, role TEXT);
        ''')
        self._cx.commit()
    
    def clear_table(self):
        self._cu.execute("DROP TABLE Users")
        self._cx.commit()
        self._initialize_table()
    
    def new_employee(self, first_name: str, last_name: str, age: int):
        max_id = self._cu.execute("SELECT MAX(id) FROM Users").fetchone()[0]
        id = max_id + 1 if max_id is not None else 0
        self._cu.execute("INSERT INTO Users (id, first_name, last_name, age, role) VALUES (?, ?, ?, ?, ?)", (id, first_name, last_name, age, "employee"))
        self._cx.commit()
        return id
    
    def new_hr(self, first_name: str, last_name: str, age: int):
        max_id = self._cu.execute("SELECT MAX(id) FROM Users").fetchone()[0]
        id = max_id + 1 if max_id is not None else 0
        self._cu.execute("INSERT INTO Users (id, first_name, last_name, age, role) VALUES (?, ?, ?, ?, ?)", (id, first_name, last_name, age, "hr"))
        self._cx.commit()
        return id
    
    def get_by_id(self, id: int):
        self._cu.execute("SELECT * FROM Users WHERE id = ?", (id,))
        user = self._cu.fetchone()
        if user:
            if user[4] == "employee":
                user = Employee(user[0], user[1], user[2], user[3])
            elif user[4] == "hr":
                user = Hr(user[0], user[1], user[2], user[3])
            return user
        return None

    def get_all_users(self):
        self._cu.execute("SELECT * FROM Users")
        users = []
        for user in self._cu.fetchall():
            if user[4] == "employee":
                users.append(Employee(user[0], user[1], user[2], user[3]))
            elif user[4] == "hr":
                users.append(Hr(user[0], user[1], user[2], user[3]))
        return users
    
    def get_all_employees(self):
        self._cu.execute("SELECT * FROM Users WHERE role = 'employee'")
        users = []
        for user in self._cu.fetchall():
            users.append(Employee(user[0], user[1], user[2], user[3]))
        return users