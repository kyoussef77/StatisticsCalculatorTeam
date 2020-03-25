from Calculator.calculator import Calculator
from StatisticsOperations.StatisticsOperations import *


class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean.mean(data)
        return self.Result

    def median(self, data):
        self.Result = Median.median(data)
        return self.Result

    def variance(self,data):
        self.Result = Variance.variance(data)
        return self.Result

    def standardDeviation(self,data):
        self.Result = StandardDeviation.standardDeviation(data)
        return self.Result