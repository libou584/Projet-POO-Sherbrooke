from models.Repositories.BaseRepository import BaseRepository


class DaysOffRepository(BaseRepository):
    def __init__(self, db_name="database.db"):
        super().__init__(db_name)
        self._initialize_database()

    def _initialize_database(self):
        self._cu.execute('''
            CREATE TABLE IF NOT EXISTS DaysOff (employee_id INT, day DATE, status TEXT, hr_id INT);
        ''')
        self._cx.commit()
    
    def clear_table(self):
        self._cu.execute("DROP TABLE DaysOff")
        self._cx.commit()
        self._initialize_database()
    
    def add_booked_day(self, employee_id: int, date: str)-> bool:
        self._cu.execute("SELECT COUNT(*) FROM DaysOff WHERE employee_id = ? AND day = ?", (employee_id, date))
        count = self._cu.fetchone()[0]
        if count == 0:
            self._cu.execute("INSERT INTO DaysOff (employee_id, day, status, hr_id) VALUES (?, ?, ?, ?)", (employee_id, date, "waiting", -1))
            self._cx.commit()
            return True
        return False
    
    def get_booked_days_by_employee_id(self, employee_id: int):
        self._cu.execute("SELECT day, status, hr_id FROM DaysOff WHERE employee_id = ? ORDER BY day", (employee_id,))
        return self._cu.fetchall()

    def get_booked_days_by_hr_id(self, hr_id: int):
        self._cu.execute("SELECT employee_id, day, status FROM DaysOff WHERE hr_id = ? ORDER BY employee_id, day", (hr_id,))
        return self._cu.fetchall()
    
    def get_all_booked_days(self):
        self._cu.execute("SELECT * FROM DaysOff ORDER BY employee_id, day")
        return self._cu.fetchall()
    
    def approve_day_off(self, employee_id: int, date: str, hr_id: int):
        self._cu.execute("UPDATE DaysOff SET status = 'approved', hr_id = ? WHERE employee_id = ? AND day = ?", (hr_id, employee_id, date))
        self._cx.commit()
    
    def reject_day_off(self, employee_id: int, date: str, hr_id: int):
        self._cu.execute("UPDATE DaysOff SET status = 'rejected', hr_id = ? WHERE employee_id = ? AND day = ?", (hr_id, employee_id, date))
        self._cx.commit()