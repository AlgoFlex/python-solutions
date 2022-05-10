from algorithms.recursion.flatten_list import flatten_list


def test_flatten_list_01():
    my_list = [
        'Memorial University of Newfoundland',
        'University of Prince Edward Island',
        [
            'University of Toronto',
            'University of Ottawa',
            'University of Waterloo'
        ]
    ]
    exp = [
        'Memorial University of Newfoundland',
        'University of Prince Edward Island',
        'University of Toronto',
        'University of Ottawa',
        'University of Waterloo'
    ]

    assert flatten_list(my_list) == exp


def test_flatten_list_02():
    my_list = []
    exp = []

    assert flatten_list(my_list) == exp


def test_flatten_list_03():
    my_list = [
        [
            'University of Toronto',
            'University of Ottawa',
            'University of Waterloo'
        ],
        [
            'University of Alberta',
            'University of Calgary'
        ]
    ]
    exp = [
        'University of Toronto',
        'University of Ottawa',
        'University of Waterloo',
        'University of Alberta',
        'University of Calgary'
    ]

    assert flatten_list(my_list) == exp
