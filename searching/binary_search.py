"""Binary Search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: [-1, 0, 1, 2, 3, 4, 5], 1
Output: 2

Input: [-1, 0, 1, 2, 3, 4, 5], -2
Output: -1
"""


def binary_search(nums, target):
    size = len(nums)
    left = 0
    right = size - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
