import unittest
import tempfile
import os

from app.database import Database
from app.student_service import StudentService


class TestStudentServiceIntegration(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()

        db_path = os.path.join(
            self.temp.name,
            "integration_test.db"
        )

        self.database = Database(db_path)
        self.service = StudentService(self.database)

    def tearDown(self):
        self.temp.cleanup()

    def test_add_and_get_student(self):
        # Add student through StudentService
        result = self.service.add_student(
            101,
            "Ravi",
            22,
            "CSE"
        )

        self.assertTrue(result)

        # Retrieve student from database through StudentService
        student = self.service.get_student(101)

        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Ravi")
        self.assertEqual(student[2], 22)
        self.assertEqual(student[3], "CSE")

    def test_add_update_and_get_student(self):
        # Add student
        self.service.add_student(
            102,
            "Sita",
            21,
            "ECE"
        )

        # Update student
        result = self.service.update_student(
            102,
            "Sita Sharma",
            22,
            "CSE"
        )

        self.assertTrue(result)

        # Get updated student
        student = self.service.get_student(102)

        self.assertEqual(student[1], "Sita Sharma")
        self.assertEqual(student[2], 22)
        self.assertEqual(student[3], "CSE")


if __name__ == "__main__":
    unittest.main()