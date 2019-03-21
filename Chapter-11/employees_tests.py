import unittest
from employee import Employee


class TestEmployees(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('John', 'Goure', 70000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEquals(self.employee.salary, 75000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEquals(self.employee.salary, 80000)

unittest.main()
