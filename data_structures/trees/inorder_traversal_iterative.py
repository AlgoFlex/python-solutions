from __future__ import annotations
from typing import List, TypeVar
from data_structures.node import TreeNode
from data_structures.stacks import Stack

T = TypeVar('T')


def inorder_traversal_iterative(root: TreeNode[T]) -> List[T]:
    result: List[T] = []
    stack: Stack = Stack()
    node: TreeNode[T] = root

    while node is not None or stack.is_empty() is not True:
        if node is not None:
            stack.push(node)
            node = node.get_left()
        else:
            node = stack.pop().get_value()
            result.append(node.get_value())
            node = node.get_right()

    return result
