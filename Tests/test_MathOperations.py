import unittest

from Calculator.calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(4, 1)
        self.assertEqual(3, result)

    def test_calculator_return_division(self):
        result = self.calculator.Division(15,5)
        self.assertEqual(3,result)