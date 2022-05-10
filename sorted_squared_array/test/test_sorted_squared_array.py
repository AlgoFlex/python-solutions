from sorted_squared_array.sorted_squared_array import sorted_squared_array


def test_sorted_squared_array():
    nums = [-5, -2, -1, 2, 3, 4]
    exp = [1, 4, 4, 9, 16, 25]

    assert sorted_squared_array(nums) == exp

    nums = [-5, -3, 2, 3, 10]
    exp = [4, 9, 9, 25, 100]

    assert sorted_squared_array(nums) == exp

    nums = [1, 2, 3, 4, 5]
    exp = [1, 4, 9, 16, 25]

    assert sorted_squared_array(nums) == exp

    nums = [-1, -2, -3, -4, -5]
    exp = [1, 4, 9, 16, 25]

    assert sorted_squared_array(nums) == exp
