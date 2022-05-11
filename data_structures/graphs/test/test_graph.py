from data_structures.node import GraphNode
from data_structures.graphs import Graph


def test_graph():
    node_a = GraphNode('A')
    node_b = GraphNode('B')
    node_c = GraphNode('C')

    graph = Graph([node_a, node_b, node_c])

    assert graph.vertices == [node_a, node_b, node_c]

    graph.add_edge(node_a, node_b)

    assert node_b in node_a.children
    assert node_a in node_b.children

    graph.remove_edge(node_a, node_b)

    assert node_a not in node_b.children
    assert node_b not in node_a.children