from recursion.sum_to_n import sum_to_n


def test_sum_to_n():
    for n in range(100, 1):
        assert sum_to_n(n) == sum(range(n))
       