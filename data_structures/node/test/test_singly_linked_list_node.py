from data_structures.node import SinglyLinkedListNode


def test_singly_linked_list_node():
    a, b, c = SinglyLinkedListNode(1), SinglyLinkedListNode(2), SinglyLinkedListNode(3)
    a.set_next(b)
    b.set_next(c)

    assert a.get_value() == 1
    assert a.get_next() == b
    assert b.get_value() == 2
    assert b.get_next() == c
    assert c.get_next() is None
