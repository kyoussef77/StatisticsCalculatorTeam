import unittest
from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistics_calculator_return_mean(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mean(data)
        self.assertEqual(3, result)

    def test_statistics_calculator_return_median(self):
        data = [1,2, 3]
        result = self.statistics.median(data)
        self.assertEqual(2,result)

    def test_statistics_calculator_return_variance(self):
        data = [1,2,3,4,5,6]
        result = self.statistics.variance(data)
        self.assertEqual(2.9166666666666665,result)

    def test_statistics_calculator_return_standard_deviation(self):
        data = [1,2,3,4,5,6]
        result = self.statistics.standardDeviation(data)
        self.assertEqual(1.2682658081265845, result)