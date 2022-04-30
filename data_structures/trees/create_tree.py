from __future__ import annotations
from typing import TypeVar, List
from data_structures.trees import Tree, TreeNode

T = TypeVar('T')


def create_tree(arr: List[T]) -> TreeNode[T]:
    return _create_tree_util(arr, 0)


def _create_tree_util(arr: List[T], start: int):
    left = 2 * start + 1
    right = 2 * start + 2
    tree = Tree(arr[start])
    current_node = tree.get_root()

    if left < len(arr):
        current_node.set_left(_create_tree_util(arr, left))

    if right < len(arr):
        current_node.set_right(_create_tree_util(arr, right))

    return current_node
