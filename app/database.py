import sqlite3

class Database:
    def __init__(self, path="students.db"):
        self.path = path
        self._initialize()

    def _initialize(self):
        conn = sqlite3.connect(self.path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        """)
        conn.commit()
        conn.close()

    def connect(self):
        return sqlite3.connect(self.path)