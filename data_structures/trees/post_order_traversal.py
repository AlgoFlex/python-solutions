from __future__ import annotations
from typing import List, TypeVar
from data_structures.trees import TreeNode

T = TypeVar('T')


def post_order_traversal(root: TreeNode[T]) -> List[T]:
    result = []
    _post_order_traversal_util(result, root)

    return result


def _post_order_traversal_util(result: List[T], node: TreeNode[T]) -> None:
    if node is None:
        return None

    _post_order_traversal_util(result, node.get_left())
    _post_order_traversal_util(result, node.get_right())
    result.append(node.get_value())
