from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;
from MathOperations.multiplication import Multiplication;
from MathOperations.division import Division;


def Sum(a, b):
    return Addition.sum(a, b)


def Difference(a, b):
    return Subtraction.difference(a, b)


def Product(a, b):
    return Multiplication.product(a, b)


def Quotient(a, b):
    return Division.quotient(a, b)



