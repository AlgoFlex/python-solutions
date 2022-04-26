"""Fibonacci

Given an integer n, return the nth fibonacci number

In mathematics, the Fibonacci numbers, are integers
which follow a specific sequence in which each number
is the sum of the two preceding ones:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

https://en.wikipedia.org/wiki/Fibonacci_number

Input: n = 0
Output: 0

Input: n = 1
Output: 1

Input: n = 7
Output: 13

"""


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
