from data_structures.node import Node


def test_node():
    n = Node("1")
    assert n.get_value() == "1"

    n = Node(1)
    assert n.get_value() == 1

