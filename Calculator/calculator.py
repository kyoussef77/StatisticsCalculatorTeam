from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;
from MathOperations.division import Division

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Division(self, a, b):
        self.Result = Division.quotient(a, b)
        return self.Result