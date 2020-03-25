from StatisticsOperations.Mean import Mean
from StatisticsOperations.Median import Median
from StatisticsOperations.mode import Mode
from StatisticsOperations.skew import Skew
from StatisticsOperations.variance import Variance
from StatisticsOperations.StandardDeviation import StandardDeviation

def mean(data):
    return Mean.mean(data)

def median(data):
    return Median.median(data)
  
def mode(data):
    return Mode.mode(data)

def skew(data, axis, bias):
    return Skew.skew(data, axis, bias)

def variance(data):
    return Variance.variance(data)

def standardDeviation(data):
    return StandardDeviation.standardDeviation(data)

