"""Sum to n

Given a positive integer number, return the sum of
all the numbers up to and inclusive of n.

Input: 5
Output: 15

Input: 1
Output: 1

Input: 7
Output: 28

Constraints:
1 <= n <= 100
"""


def sum_to_n(n):
    if n == 1:
        return 1

    return n + sum_to_n(n - 1)
