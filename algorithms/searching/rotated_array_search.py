from typing import List

"""Search in a Rotated Sorted Array

Given a sorted array which is rotated at some random pivot point and a target,
return the index of the target or -1 if not found in the array.

Input: [4,5,6,7,0,1,2], target = 5
Output: 1

Input: [4,5,6,7,0,1,2], target = 10
Output: -1

Constraints:

- You can assume there are no duplicates in the array.
- Runtime complexity must be in the order of O(log n).

"""


def rotated_array_search(nums: List[int], target: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       nums(array): Input array to search
       target(int): Target element
    Returns:
       int: Index or -1
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        lower, upper = nums[left], nums[right]
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if upper < lower:
                if target < upper:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right = mid - 1
        else:
            if upper < lower:
                if target < upper:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left = mid + 1

    return -1
