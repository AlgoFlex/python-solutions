from typing import List, Tuple

"""Max and Min in an Unsorted Array

Given a list of unsorted integers, find and return the smallest and the largest number in the list.

Input : [0,1,2,3,4,5,6,7,8,9]
Output: 0, 9

Constraints:

The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Hint: Is it possible to find the max and min in a single traversal?

"""


def get_min_max(nums: List[int]) -> Tuple[int, int]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       nums(list): list of integers containing one or more integers
    """
    min, max = nums[0], nums[0]

    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num

    return min, max
