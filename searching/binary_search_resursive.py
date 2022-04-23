"""Binary Search

Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write a recursive algorithm

Input: [-1, 0, 1, 2, 3, 4, 5], 1
Output: 2

Input: [-1, 0, 1, 2, 3, 4, 5], -2
Output: -1
"""


def binary_search_recursive(nums, target):
    size = len(nums)
    left = 0
    right = size - 1

    return __binary_search(nums, left, right, target)


def __binary_search(nums, left, right, target):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return __binary_search(nums, mid + 1, right, target)
    else:
        return __binary_search(nums, left, mid - 1, target)
