from data_structures.linked_list import DoublyLinkedListNode


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
