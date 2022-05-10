"""Power Set

Given a list of strings, return a list of all
subsets of the values in a list.

Input: ['a', 'b', 'c']
Output:
[
  ['a', 'b', 'c'],
  ['a', 'b'],
  ['a', 'c'],
  ['a'],
  ['b', 'c'],
  ['b'],
  ['c'],
  []
]

Input: []:
Output: [[]]

Input: ['a']
Output: [[], ['a']]

"""


def power_set(str_list):
    if len(str_list) == 0:
        return [[]]

    power_set_without_first = power_set(str_list[1:])
    power_set_with_first = [[str_list[0]] + s for s in power_set_without_first]

    return power_set_with_first + power_set_without_first
