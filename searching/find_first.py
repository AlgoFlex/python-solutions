"""Find First Index of Target

Given a sorted array that may have duplicate values,
use binary search to find the first index of a given value.

Return -1 if target cannot be found.

Input: [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15], target = 7
Output: 3

Input: [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15], target = 9
Output: -1
"""
from typing import List


def find_first(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if target == arr[mid]:
            ans = mid
            right = mid - 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return ans
