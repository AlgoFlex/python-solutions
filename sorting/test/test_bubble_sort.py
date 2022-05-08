from sorting.bubble_sort import bubble_sort


def test_bubble_sort():
    nums = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
    output = [3, 9, 12, 13, 13, 16, 19, 22, 25, 45, 46, 46, 48, 49, 49, 55, 55, 56, 56]

    assert bubble_sort(nums) == output
