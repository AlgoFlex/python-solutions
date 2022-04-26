"""Flatten List

Given a list of strings and nested lists of string
return a list without the nested lists while maintaining
the values in the list

Input:
[
    'Memorial University of Newfoundland',
    'University of Prince Edward Island',
    [
        'University of Toronto',
        'University of Ottawa',
        'University of Waterloo'
    ]
]
Output:
[
    'Memorial University of Newfoundland',
    'University of Prince Edward Island',
    'University of Toronto',
    'University of Ottawa',
    'University of Waterloo'
]

Input:
[
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
Output:
[
    'University of Toronto',
    'University of Ottawa',
    'University of Waterloo',
    'University of Alberta',
    'University of Calgary'
]

Input: []
Output: []

"""


def flatten_list(my_list):
    result = []

    for item in my_list:
        if isinstance(item, list):
            nested_list = flatten_list(item)
            result += nested_list
        else:
            result.append(item)

    return result
