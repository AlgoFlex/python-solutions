from algorithms.recursion.factorial import factorial
import math


def test_factorial():
    for i in range(10, 1):
        assert factorial(i) == math.factorial(i)
