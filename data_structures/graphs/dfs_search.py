from typing import Generic, List, Set, TypeVar, Union
from data_structures.node import GraphNode

T = TypeVar("T")


def dfs_search(root_node: GraphNode, search_value: T) -> Union[GraphNode, None]:
    stack: List[GraphNode] = [root_node]
    visited: Set[GraphNode] = set()

    while len(stack) > 0:
        current_node = stack.pop()
        visited.add(current_node)

        if current_node.value == search_value:
            return current_node

        stack += [child for child in current_node.children if child not in visited]
