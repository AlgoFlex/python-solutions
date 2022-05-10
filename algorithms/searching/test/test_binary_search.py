from algorithms.searching.binary_search_iterative import binary_search_iterative


def test_binary_search_01():
    nums = [-1, 0, 1, 2, 3, 4, 5]
    target = 1

    result = binary_search_iterative(nums, target)
    exp = 2

    assert result == exp


def test_binary_search_02():
    nums = [-1, 0, 1, 2, 3, 4, 5]
    target = -2

    result = binary_search_iterative(nums, target)
    exp = -1

    assert result == exp
