from __future__ import annotations
from typing import List, TypeVar
from data_structures.trees import TreeNode

T = TypeVar('T')


def inorder_traversal(root: TreeNode[T]) -> List[T]:
    result = []
    _inorder_traversal_util(result, root)

    return result


def _inorder_traversal_util(result: List[T], node: TreeNode[T]) -> None:
    if node is None:
        return

    _inorder_traversal_util(result, node.get_left())
    result.append(node.get_value())
    _inorder_traversal_util(result, node.get_right())
