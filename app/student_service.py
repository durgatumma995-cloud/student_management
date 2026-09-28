import sqlite3

class StudentService:
    def __init__(self, database):
        self.db = database

    def add_student(self, id, name, age, grade):
        if not name or str(name).strip() == "":
            raise ValueError("Name cannot be empty")
        if age < 15:
            raise ValueError("Age must be >= 15")

        conn = self.db.connect()
        try:
            conn.execute(
                "INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)",
                (id, name, age, grade)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            raise Exception(f"Duplicate ID: {e}")
        finally:
            conn.close()

    def get_student(self, id):
        conn = self.db.connect()
        try:
            cursor = conn.execute("SELECT * FROM students WHERE id = ?", (id,))
            row = cursor.fetchone()
            return row
        finally:
            conn.close()

    def get_all_students(self):
        conn = self.db.connect()
        try:
            cursor = conn.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            return rows
        finally:
            conn.close()

    def update_student(self, id, name, age, grade):
        conn = self.db.connect()
        try:
            cursor = conn.execute(
                "UPDATE students SET name=?, age=?, grade=? WHERE id=?",
                (name, age, grade, id)
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    def delete_student(self, id):
        conn = self.db.connect()
        try:
            cursor = conn.execute("DELETE FROM students WHERE id=?", (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()