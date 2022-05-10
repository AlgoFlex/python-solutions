from algorithms.searching.linear_search import linear_search


def test_linear_search():
    nums = [5, 2, 4, 6, 1, 3]
    target = 10
    exp = None

    assert linear_search(nums, target) is None

    nums = [5, 2, 4, 6, 1, 3]
    target = 4
    exp = 2

    assert linear_search(nums, target) == exp