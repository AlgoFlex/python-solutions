from data_structures.graphs import Graph, bfs_search
from data_structures.node import GraphNode


def test_bfs_search():
    node_a = GraphNode('A')
    node_b = GraphNode('B')
    node_c = GraphNode('C')

    graph = Graph([node_a, node_b, node_c])

    graph.add_edge(node_a, node_b)
    graph.add_edge(node_a, node_c)
    graph.add_edge(node_b, node_c)

    assert bfs_search(node_a, 'A') == node_a
    assert bfs_search(node_a, 'B') == node_b
    assert bfs_search(node_a, 'C') == node_c
    assert bfs_search(node_a, 'D') is None
