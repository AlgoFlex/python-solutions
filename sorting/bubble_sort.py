from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for idx in range(1, len(nums)):
            current = nums[idx]
            prev = nums[idx - 1]

            if prev > current:
                nums[idx] = prev
                nums[idx - 1] = current

    return nums
