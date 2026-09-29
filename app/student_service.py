from app.database import Database
class StudentService:
    def __init__(self, db):
        self.db = db
    def add_student(self, id, name, age, branch):
        return self.db.add_student(id, name, age, branch)
    def get_student(self, id):
        return self.db.get_student(id)
    def get_all_students(self):
        return self.db.get_all_students()
    def update_student(self, id, name, age, branch):
        return self.db.update_student(id, name, age, branch)
    def delete_student(self, id):
        return self.db.delete_student(id)
