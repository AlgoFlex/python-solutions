from algorithms.searching.find_last import find_last


def test_find_last_01():
    arr = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
    target = 7

    assert find_last(arr, target) == 5


def test_find_last_02():
    arr = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
    target = 9

    assert find_last(arr, target) == -1


def test_find_last_03():
    arr = [1]
    target = 1

    assert find_last(arr, target) == 0
