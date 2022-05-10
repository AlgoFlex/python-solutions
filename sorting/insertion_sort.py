from typing import List

"""
INSERTION_SORT(A)
for i = 0 to n - 1
    key = A[0]
    // Insert A[i] into the sorted subarray A[1 : i – 1].
    j = i - 1
    while j >= 0 and A[j] > key
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key
"""


def insertion_sort(nums: List[int]) -> None:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
