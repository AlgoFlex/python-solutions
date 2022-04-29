from recursion.binary_search import binary_search


def test_binary_search_01():
    nums = [-1, 0, 1, 2, 3, 4, 5]
    target = -2

    result = binary_search(nums, target)
    exp = -1

    assert result == exp


def test_binary_search_02():
    nums = [-1, 0, 1, 2, 3, 4, 5]
    target = 1

    result = binary_search(nums, target)
    exp = 2

    assert result == exp

