from models.Repositories.BaseRepository import BaseRepository


class NotificationRepository(BaseRepository):
    """
    Repository for managing notifications.
    """

    def __init__(self, db_name="database.db"):
        super().__init__(db_name)
        self._initialize_table()

    def _initialize_table(self):
        self._cu.execute('''
            CREATE TABLE IF NOT EXISTS Notifications (id INT PRIMARY KEY, user_id INT, message TEXT);
        ''')
        self._cx.commit()

    def clear_table(self):
        self._cu.execute("DROP TABLE Notifications")
        self._cx.commit()
        self._initialize_table()
    
    def send_employee_notification(self, user_id: int, message: str):
        self._cu.execute("SELECT MAX(id) FROM Notifications")
        max_id = self._cu.fetchone()[0]
        next_id = 0 if max_id is None else max_id + 1
        self._cu.execute("INSERT INTO Notifications (id, user_id, message) VALUES (?, ?, ?)", (next_id, user_id, message))
        self._cx.commit()
    
    def send_hr_notification(self, message: str):
        self._cu.execute("SELECT MAX(id) FROM Notifications")
        max_id = self._cu.fetchone()[0]
        next_id = 0 if max_id is None else max_id + 1
        self._cu.execute("INSERT INTO Notifications (id, user_id, message) VALUES (?, ?, ?)", (next_id, -1, message))
        self._cx.commit()

    def get_all_notifications(self):
        self._cu.execute("SELECT * FROM Notifications")
        return self._cu.fetchall()