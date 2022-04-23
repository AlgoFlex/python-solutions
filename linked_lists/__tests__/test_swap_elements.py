import pytest

from linked_lists.swap_elements import Solution
from data_structures.linked_list import SinglyLinkedList


def test_swap_elements_01():
    sll = SinglyLinkedList()

    head_node = sll.get_head()

    assert Solution.swap_elements(head_node, 2, 4) is None


def test_swap_nodes_02():
    items = [1, 2, 3, 4, 5]
    sll = SinglyLinkedList(items)

    head_node = sll.get_head()
    result = Solution.swap_nodes(head_node, 2, 4)
    exp = SinglyLinkedList([1, 4, 3, 2, 5])

    assert result.get_value() == 1
    assert str(sll) == str(exp)


def test_swap_nodes_03():
    items = [1, 2, 3, 4, 5]
    sll = SinglyLinkedList(items)

    head_node = sll.get_head()
    results = [3, 2, 1, 4, 5]
    new_head = Solution.swap_nodes(head_node, 1, 3)

    for item in results:
        assert new_head.get_value() == item
        new_head = new_head.get_next()


def test_swap_nodes_04():
    items = [1, 2, 3, 4, 5]
    sll = SinglyLinkedList(items)

    head_node = sll.get_head()
    results = [1, 3, 2, 4, 5]
    new_head = Solution.swap_nodes(head_node, 2, 3)

    for item in results:
        assert new_head.get_value() == item
        new_head = new_head.get_next()


def test_swap_nodes_05():
    items = [1, 2, 3, 4, 5]
    sll = SinglyLinkedList(items)

    head_node = sll.get_head()
    with pytest.raises(ValueError):
        Solution.swap_nodes(head_node, None, 3)
