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
        
    def test_statistics_calculator_return_mode(self):
        data = [1, 2, 3, 3, 4, 5]
        result = self.statistics.mode(data)
        self.assertEqual(3, result)

    def test_statistics_calculator_return_NoMode(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mode(data)
        self.assertEqual('no mode', result)
        
    def test_statistics_calculator_return_skew(self):
        data = [3, 5, 6, 5, 3, 2, 1, 40]
        result = self.statistics.skew(data, None, None)
        self.assertEqual(2.734386516915545, result)
        
    def test_statistics_calculator_return_variance(self):
        data = [1,2,3,4,5,6]
        result = self.statistics.variance(data)
        self.assertEqual(2.9166666666666665,result)

    def test_statistics_calculator_return_standard_deviation(self):
        data = [1,2,3,4,5,6]
        result = self.statistics.standardDeviation(data)
        self.assertEqual(1.2682658081265845, result)

    def test_statistics_calculator_return_covariance(self):
        data1 = [1,2,3,4]
        data2 = [1,2,4,5]
        result = self.statistics.covariance(data1,data2)
        self.assertEqual(2.333333333333333, result)

    def test_statistics_calculator_return_sample_correlation(self):
        data1 = [1,2,3,4]
        data2 = [1,2,4,5]
        result = self.statistics.samplecorrelation(3,data1,data2)
        self.assertEqual(0.1446890230103591, result)




