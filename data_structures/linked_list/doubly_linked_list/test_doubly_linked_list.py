from doubly_linked_list import DoublyLinkedList


def test_prepend():
    dll = DoublyLinkedList()
    items = [3, 2, 1]

    for item in items:
        dll.prepend(item)

    current_node = dll.get_head()
    assert current_node.get_value() == 1
    assert current_node.get_prev() is None

    for item in reversed(items):
        assert current_node.get_value() == item
        current_node = current_node.get_next()

    assert dll.get_tail().get_value() == 3
    assert dll.get_tail().get_next() is None


def test_append():
    dll = DoublyLinkedList()
    items = [1, 2, 3]

    for item in items:
        dll.append(item)

    current_node = dll.get_head()
    assert current_node.get_value() == 1
    assert current_node.get_prev() is None

    for item in items:
        assert current_node.get_value() == item
        current_node = current_node.get_next()

    assert dll.get_tail().get_value() == 3
    assert dll.get_tail().get_next() is None


def test_remove_head():
    dll = DoublyLinkedList()
    items = [1, 2, 3]

    for item in items:
        dll.append(item)

    for i, item in enumerate(items):
        assert dll.remove_head().get_value() == items[i]
        assert len(dll) == len(items) - (i + 1)

    assert dll.get_head() is None
    assert dll.get_tail() is None


def test_remove_tail():
    dll = DoublyLinkedList()
    items = [1, 2, 3]

    for item in items:
        dll.append(item)

    for i, item in enumerate(reversed(items)):
        assert dll.remove_tail().get_value() == item
        assert len(dll) == len(items) - (i + 1)

    assert dll.get_head() is None
    assert dll.get_tail() is None


def test_remove():
    items = [1, 2, 3, 4, 5]
    dll = DoublyLinkedList()

    for item in items:
        dll.append(item)

    removed_node = dll.remove(3)
    assert removed_node.get_value() == 3
    assert len(dll) == 4

    removed_node = dll.remove(1)
    assert removed_node.get_value() == 1
    assert dll.get_head().get_value() == 2
    assert len(dll) == 3

    removed_node = dll.remove(5)
    assert removed_node.get_value() == 5
    assert dll.get_tail().get_value() == 4
    assert len(dll) == 2

    removed_node = dll.remove(2)
    assert removed_node.get_value() == 2
    assert dll.get_head().get_value() == 4
    assert dll.get_tail().get_value() == 4
    assert len(dll) == 1

    removed_node = dll.remove(5)
    assert removed_node is None


def test_length():
    dll = DoublyLinkedList()
    items = [3, 2, 1]

    for i, item in enumerate(items):
        dll.prepend(item)
        assert len(dll) == i + 1


def test_to_string():
    dll = DoublyLinkedList()
    items = [1, 2, 3]

    for item in items:
        dll.append(item)

    assert str(dll) == "None<-1<=>2<=>3->None"
