import unittest
from random import randint, seed, sample

from PopulationSampling.Cochran import Cochran


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(4)
        self.testData = sample(range(0, 50), 10)


    def test_Cochran(self):
        result = Cochran.cochran(3, self.testData, 4)
        self.assertEqual(result, 0.37809484249342223)


if __name__ == '__main__':
    unittest.main()