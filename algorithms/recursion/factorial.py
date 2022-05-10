"""Factorial

Given a positive integer as input, return the product
of every integer from 1 up to the input. If the input
is less than 2, return 1.

Input: 4
Output: 24

Input: 2
Output: 2

Input: 1
Output: 1

"""


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)
