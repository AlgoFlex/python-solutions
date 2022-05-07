from searching.rotated_array_search import rotated_array_search


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_rotated_array_search():
    tests = [
        [[6, 7, 8, 9, 10, 1, 2, 3, 4], 6, 0],
        [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1, 5],
        [[6, 7, 8, 1, 2, 3, 4], 8, 2],
        [[6, 7, 8, 1, 2, 3, 4], 1, 3],
        [[6, 7, 8, 1, 2, 3, 4], 10, -1]
    ]

    for test in tests:
        arr, target, exp = test
        assert rotated_array_search(arr, target) == exp
