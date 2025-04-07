import sqlite3


class BaseRepository:

    def __init__(self, db_name="database.db"):
        self._cx = sqlite3.connect(db_name, check_same_thread=False)
        self._cu = self._cx.cursor()
    
    def __del__(self):
        self._cx.close()