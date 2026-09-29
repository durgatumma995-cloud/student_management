import unittest, tempfile, os
from app.database import Database
from app.student_service import StudentService

class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = Database(os.path.join(self.temp.name, "test.db"))
        self.service = StudentService(self.db)
    def tearDown(self):
        self.db.close()
        self.temp.cleanup()

    # 11 TESTS START
    def test_01_add(self):
        self.assertTrue(self.service.add_student(1, "Ravi", 20, "CSE"))
    def test_02_get(self):
        self.service.add_student(1, "Ravi", 20, "CSE")
        self.assertEqual(self.service.get_student(1)[1], "Ravi")
    def test_03_get_all_1(self):
        self.service.add_student(1, "A", 20, "CSE")
        self.assertEqual(len(self.service.get_all_students()), 1)
    def test_04_get_all_2(self):
        self.service.add_student(1, "A", 20, "CSE")
        self.service.add_student(2, "B", 21, "ECE")
        self.assertEqual(len(self.service.get_all_students()), 2)
    def test_05_update(self):
        self.service.add_student(1, "Ravi", 20, "CSE")
        self.service.update_student(1, "Ravi Kumar", 21, "ECE")
        self.assertEqual(self.service.get_student(1)[1], "Ravi Kumar")
    def test_06_delete(self):
        self.service.add_student(1, "Ravi", 20, "CSE")
        self.service.delete_student(1)
        self.assertIsNone(self.service.get_student(1))
    def test_07_add_duplicate(self):
        self.service.add_student(1, "Ravi", 20, "CSE")
        self.assertFalse(self.service.add_student(1, "Ravi", 20, "CSE"))
    def test_08_add_and_get(self):
        self.service.add_student(101, "Sita", 22, "CSE")
        self.assertEqual(self.service.get_student(101)[2], 22)
    def test_09_add_update_get(self):
        self.service.add_student(102, "Sita", 21, "ECE")
        self.service.update_student(102, "Sita Sharma", 22, "CSE")
        self.assertEqual(self.service.get_student(102)[1], "Sita Sharma")
    def test_10_add_delete_get(self):
        self.service.add_student(103, "Arjun", 23, "MECH")
        self.service.delete_student(103)
        self.assertIsNone(self.service.get_student(103))
    def test_11_branch_check(self):
        self.service.add_student(104, "A", 20, "CSE")
        s = self.service.get_student(104)
        self.assertEqual(s[3], "CSE")
