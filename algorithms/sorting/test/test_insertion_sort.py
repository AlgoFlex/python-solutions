from algorithms.sorting.insertion_sort import insertion_sort


def test_insertion_sort():
    nums = [1]
    exp = [1]
    insertion_sort(nums)
    assert nums == exp

    nums = [5, 2, 4, 6, 1, 3]
    exp = [1, 2, 3, 4, 5, 6]
    insertion_sort(nums)

    assert nums == exp

    nums = [31, 41, 59, 26, 41, 58]
    exp = [26, 31, 41, 41, 58, 59]
    insertion_sort(nums)

    assert nums == exp
