import random

from searching.get_min_max import get_min_max


def test_get_min_max_01():
    nums = [i for i in range(0, 10)]
    random.shuffle(nums)

    assert get_min_max(nums) == (0, 9)
