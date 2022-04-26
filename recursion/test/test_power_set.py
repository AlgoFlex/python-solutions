from recursion.power_set import power_set


def test_power_set_01():
    str_list = []
    exp = [[]]

    assert power_set(str_list) == exp


def test_power_set_02():
    str_list = ['a']
    exp = [['a'], []]

    assert power_set(str_list) == exp


def test_power_set_03():
    str_list = ['a', 'b', 'c']
    exp = [
        ['a', 'b', 'c'],
        ['a', 'b'],
        ['a', 'c'],
        ['a'],
        ['b', 'c'],
        ['b'],
        ['c'],
        []
    ]

    assert power_set(str_list) == exp
