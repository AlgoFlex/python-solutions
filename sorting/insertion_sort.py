from typing import List


def insertion_sort(nums: List[int]) -> None:
    if len(nums) == 1:
        return

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
