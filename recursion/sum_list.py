"""Sum List

Given a list of integers, return the sum of the elements
in the list using recursive strategy.

Input: [1, 2, 3, 4, 5]
Output: 15

Input: [1]
Output: 1

Input: []
Output: 0

"""


def sum_list(nums):
    if len(nums) == 0:
        return 0

    return nums[0] + sum_list(nums[1:])
