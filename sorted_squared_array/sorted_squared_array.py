"""Sorted Squared Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares
of each number sorted in non-decreasing order.

Input: [-5, -2, -1, 2, 3, 4]
Output: [1, 4, 4, 9, 16, 25]

Input: nums = [-5,-3,2,3,10]
Output: [4,9,9,25,100]

Constraint: Time complexity of the solution should be O(n)
"""
from typing import List


def sorted_squared_array(nums: List[int]) -> List[int]:
    size = len(nums)
    results = [0] * size
    l, r = 0, size - 1

    for i in range(size - 1, -1, -1):
        left = abs(nums[l])
        right = abs(nums[r])
        if left >= right:
            results[i] = left ** 2
            l += 1
        else:
            results[i] = right ** 2
            r -= 1

    return results
