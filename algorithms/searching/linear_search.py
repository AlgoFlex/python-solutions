from typing import List

"""
LINEAR_SEARCH(A, x)
for i = 0 to n - 1
    if A[i] == x
        return i
return NIL
"""


def linear_search(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i

    return None
