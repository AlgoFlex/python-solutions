from recursion.sum_list import sum_list


def test_sum_list_01():
    nums = []
    exp = 0

    assert sum_list(nums) == exp


def test_sum_list_02():
    nums = [1]
    exp = 1

    assert sum_list(nums) == exp


def test_sum_list_03():
    nums = [1, 2, 3, 4, 5]
    exp = 15

    assert sum_list(nums) == exp
