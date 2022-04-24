import pytest

from data_structures.stacks import Stack


def test_init():
    stack = Stack()

    assert stack.peek() is None
    assert stack.is_empty() is True
    assert stack.has_space() is True

    stack = Stack(0)

    assert stack.has_space() is False


def test_push():
    items = [1, 2, 3]
    stack = Stack(3)

    for i, item in enumerate(items):
        stack.push(item)
        assert stack.peek().get_value() == item
        assert len(stack) == i + 1

    assert stack.has_space() is False

    with pytest.raises(ValueError):
        err = stack.push(4)
        assert str(err) == "Stack overflow"


def test_pop():
    items = [1, 2, 3]
    stack = Stack()

    for item in items:
        stack.push(item)

    for item in reversed(items):
        assert stack.pop().get_value() == item

    assert stack.pop() is None
