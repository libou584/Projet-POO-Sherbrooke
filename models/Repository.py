import sqlite3

from models.Employee import Employee


class Repository:

    def __init__(self, db_name="database.db"):
        self.__cx = sqlite3.connect(db_name, check_same_thread=False)
        self.__cu = self.__cx.cursor()
        self._initialize_database()
    
    def _initialize_database(self):
        self.__cu.execute('''
            CREATE TABLE IF NOT EXISTS Users (id INT PRIMARY KEY, first_name TEXT, last_name TEXT, age INT, role TEXT);
        ''')
        self.__cx.commit()
        self.__cu.execute("SELECT * FROM Users")
        if not self.__cu.fetchall():
            self.new_employee('John', 'Doe', 25)
        self.__cu.execute('''
            CREATE TABLE IF NOT EXISTS DaysOff (employee_id INT, day DATE, status TEXT);
        ''')
        self.__cx.commit()
    
    def __del__(self):
        self.__cx.close()

    def new_employee(self, first_name: str, last_name: str, age: int):
        max_id = self.__cu.execute("SELECT MAX(id) FROM Users").fetchone()[0]
        id = max_id + 1 if max_id is not None else 0
        self.__cu.execute("INSERT INTO Users (id, first_name, last_name, age, role) VALUES (?, ?, ?, ?, ?)", (id, first_name, last_name, age, "employee"))
        self.__cx.commit()

    def get_all_users(self):
        self.__cu.execute("SELECT * FROM Users")
        users = []
        for user in self.__cu.fetchall():
            if user[4] == "employee":
                users.append(Employee(user[0], user[1], user[2], user[3]))
            else:
                users.append(user)
        return users
    
    def get_user_by_id(self, id: int):
        self.__cu.execute("SELECT * FROM Users WHERE id = ?", (id,))
        user = self.__cu.fetchone()
        if user:
            if user[4] == "employee":
                user = Employee(user[0], user[1], user[2], user[3])
            return user
        return None
    
    def add_booked_day(self, id: int, date: str)-> bool:
        self.__cu.execute("SELECT COUNT(*) FROM DaysOff WHERE employee_id = ? AND day = ?", (id, date))
        count = self.__cu.fetchone()[0]
        if count == 0:
            self.__cu.execute("INSERT INTO DaysOff (employee_id, day, status) VALUES (?, ?, ?)", (id, date, "waiting"))
            self.__cx.commit()
            return True
        return False
    
    def get_booked_days(self, id: int):
        self.__cu.execute("SELECT day, status FROM DaysOff WHERE employee_id = ? ORDER BY day", (id,))
        return self.__cu.fetchall()