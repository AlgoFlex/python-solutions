from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_portion = nums[:mid]
    right_portion = nums[mid:]

    left_portion = merge_sort(left_portion)
    right_portion = merge_sort(right_portion)

    return _merge(left_portion, right_portion)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            merged.append(right[right_idx])
            right_idx += 1
        else:
            merged.append(left[left_idx])
            left_idx += 1

    # Append any remaining elements.
    # At this point, we know at least one is empty,
    # and the remaining:
    # a) are already sorted and
    # b) all sort past our last element in merged
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged
