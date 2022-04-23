import pytest

from data_structures.linked_list import SinglyLinkedList


def test_append():
    sll = SinglyLinkedList()
    items = [1, 2, 3]

    for item in items:
        sll.append(item)

    head = sll.get_head()
    assert head.get_value() == 1
    assert head.get_next().get_value() == 2
    assert head.get_next().get_next().get_value() == 3
    assert head.get_next().get_next().get_next() is None


def test_init():
    items = [1, 2, 3]
    sll = SinglyLinkedList(items)

    current = sll.get_head()
    for item in items:
        assert current.get_value() == item
        current = current.get_next()


def test_get_head():
    sll = SinglyLinkedList()
    assert sll.get_head() is None

    sll.append(1)
    assert sll.get_head().get_value() == 1
    assert sll.get_head().get_next() is None


def test_len():
    sll = SinglyLinkedList()
    items = [1, 2, 3]

    for i, item in enumerate(items):
        sll.append(item)
        assert len(sll) == i + 1


def test_prepend():
    sll = SinglyLinkedList()
    items = [1, 2, 3]

    for item in items:
        sll.prepend(item)

    current_node = sll.get_head()
    for item in reversed(items):
        assert current_node.get_value() == item
        current_node = current_node.get_next()


def test_find():
    sll = SinglyLinkedList()
    items = [1, 2, 3]

    for item in items:
        sll.append(item)

    for i, item in enumerate(items):
        assert sll.find(item) == i

    assert sll.find(4) == -1


def test_insert():
    sll = SinglyLinkedList()
    items = [1, 2, 3]

    for item in items:
        sll.append(item)

    with pytest.raises(IndexError):
        sll.insert(4, -1)
    with pytest.raises(IndexError):
        sll.insert(4, 4)

    sll.insert(0, 0)
    assert sll.get_head().get_value() == 0

    sll.insert(4, 4)
    assert sll.find(4) == 4

    sll.insert(2.5, 2)
    assert sll.find(2.5) == 3


def test_delete():
    sll = SinglyLinkedList()
    items = [1, 2, 3, 4]

    for item in items:
        sll.append(item)

    assert sll.delete(5) is None
    assert len(sll) == len(items)

    sll.delete(1)
    assert sll.get_head().get_value() == 2

    sll.delete(3)
    assert len(sll) == 2
    assert sll.get_head().get_value() == 2
    assert sll.get_head().get_next().get_value() == 4

    sll.delete(2)
    assert sll.get_head().get_value() == 4
