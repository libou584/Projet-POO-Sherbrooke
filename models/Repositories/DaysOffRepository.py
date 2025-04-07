from models.Repositories.BaseRepository import BaseRepository


class DaysOffRepository(BaseRepository):
    def __init__(self, db_name="database.db"):
        super().__init__(db_name)
        self._initialize_database()

    def _initialize_database(self):
        self._cu.execute('''
            CREATE TABLE IF NOT EXISTS DaysOff (employee_id INT, day DATE, status TEXT);
        ''')
        self._cx.commit()
    
    def clear_table(self):
        self._cu.execute("DROP TABLE DaysOff")
        self._cx.commit()
        self._initialize_database()
    
    def add_booked_day(self, id: int, date: str)-> bool:
        self._cu.execute("SELECT COUNT(*) FROM DaysOff WHERE employee_id = ? AND day = ?", (id, date))
        count = self._cu.fetchone()[0]
        if count == 0:
            self._cu.execute("INSERT INTO DaysOff (employee_id, day, status) VALUES (?, ?, ?)", (id, date, "waiting"))
            self._cx.commit()
            return True
        return False
    
    def get_booked_days(self, id: int):
        self._cu.execute("SELECT day, status FROM DaysOff WHERE employee_id = ? ORDER BY day", (id,))
        return self._cu.fetchall()
    
    def approve_day_off(self, id: int, date: str):
        self._cu.execute("UPDATE DaysOff SET status = 'approved' WHERE employee_id = ? AND day = ?", (id, date))
        self._cx.commit()
    
    def reject_day_off(self, id: int, date: str):
        self._cu.execute("UPDATE DaysOff SET status = 'rejected' WHERE employee_id = ? AND day = ?", (id, date))
        self._cx.commit()