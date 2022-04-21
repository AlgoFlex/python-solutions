class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


def test_node():
    a, b, c = Node(1), Node(2), Node(3)
    a.set_next(b)
    b.set_next(c)

    assert a.get_value() == 1
    assert a.get_next() == b
    assert b.get_value() == 2
    assert b.get_next() == c
    assert c.get_next() is None
