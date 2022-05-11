from typing import Generic, List, Set, TypeVar, Union
from data_structures.node import GraphNode

T = TypeVar("T")


def bfs_search(root_node: GraphNode, search_value: T) -> Union[GraphNode, None]:
    queue: List[GraphNode] = [root_node]
    visited: Set[GraphNode] = set()

    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.add(current_node)

        if current_node.value == search_value:
            return current_node

        queue += [child for child in current_node.children if child not in visited]
