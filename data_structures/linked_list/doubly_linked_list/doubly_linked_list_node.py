class DoublyLinkedListNode:
    def __init__(self, value, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def get_prev(self):
        return self._prev

    def set_next(self, next_node):
        self._next = next_node

    def set_prev(self, prev_node):
        self._prev = prev_node


def test_doubly_linked_list_node():
    a, b, c = DoublyLinkedListNode(1), DoublyLinkedListNode(2), DoublyLinkedListNode(3)
    a.set_next(b)
    b.set_prev(a)
    b.set_next(c)
    c.set_prev(b)

    assert a.get_value() == 1
    assert a.get_next() == b
    assert b.get_prev() == a
    assert b.get_value() == 2
    assert b.get_next() == c
    assert c.get_prev() == b
    assert c.get_next() is None
