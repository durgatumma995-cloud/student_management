import sqlite3
class Database:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, branch TEXT)")
        self.conn.commit()
    def add_student(self, id, name, age, branch):
        try:
            self.conn.execute("INSERT INTO students VALUES (?,?,?,?)", (id, name, age, branch))
            self.conn.commit()
            return True
        except: return False
    def get_student(self, id):
        return self.conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    def get_all_students(self):
        return self.conn.execute("SELECT * FROM students").fetchall()
    def update_student(self, id, name, age, branch):
        self.conn.execute("UPDATE students SET name=?, age=?, branch=? WHERE id=?", (name, age, branch, id))
        self.conn.commit()
        return True
    def delete_student(self, id):
        self.conn.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        return True
    def close(self):
        self.conn.close()
