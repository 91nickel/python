from employe import Employee
import unittest


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Никита", "Кузнецов", 5000)

    def test_give_default_raise(self):
        start_value = self.employee.pay
        self.employee.give_raise()
        self.assertEqual(self.employee.pay - start_value, 5000)

    def test_give_custom_raise(self):
        start_value = self.employee.pay
        upper = 2500
        self.employee.give_raise(upper)
        self.assertEqual(self.employee.pay - start_value, upper)


if __name__ == "__main__":
    unittest.main()
