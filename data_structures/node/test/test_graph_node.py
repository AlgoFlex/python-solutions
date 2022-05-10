from data_structures.node import GraphNode


def test_graph_node():
    gn = GraphNode(1)

    assert gn.value == 1
    assert gn.children == []

    child = GraphNode(2)
    gn.add_child(child)

    assert child in gn.children

    gn.remove_child(child)

    assert child not in gn.children
