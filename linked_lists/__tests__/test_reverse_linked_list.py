from linked_lists.reverse_linked_list import Solution
from data_structures.linked_list import SinglyLinkedList


def test_reverse_linked_list_01():
    sll = SinglyLinkedList()

    head_node = sll.get_head()

    assert Solution.reverse_linked_list(head_node) is None


def test_reverse_linked_list_02():
    sll = SinglyLinkedList()
    sll.append(1)

    head_node = sll.get_head()

    assert Solution.reverse_linked_list(head_node).get_value() == 1


def test_reverse_linked_list_03():
    sll = SinglyLinkedList()
    items = [1, 2, 3]

    for item in items:
        sll.append(item)

    head_node = sll.get_head()

    assert Solution.reverse_linked_list(head_node).get_value() == 3
