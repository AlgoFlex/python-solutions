from algorithms.recursion.fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13
