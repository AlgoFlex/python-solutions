from __future__ import annotations
from typing import List, TypeVar
from data_structures.trees import TreeNode

T = TypeVar('T')


def pre_order_traversal(root: TreeNode[T]) -> List[T]:
    result = []
    _pre_order_util(result, root)

    return result


def _pre_order_util(result: List[T], node: TreeNode[T]):
    if node is None:
        return

    result.append(node.get_value())
    _pre_order_util(result, node.get_left())
    _pre_order_util(result, node.get_right())

