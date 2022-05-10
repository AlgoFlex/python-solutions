from algorithms.searching.find_first import find_first


def test_find_first_01():
    arr = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
    target = 7

    assert find_first(arr, target) == 3


def test_find_first_02():
    arr = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
    target = 9

    assert find_first(arr, target) == -1


def test_find_first_03():
    arr = [1]
    target = 1

    assert find_first(arr, target) == 0
