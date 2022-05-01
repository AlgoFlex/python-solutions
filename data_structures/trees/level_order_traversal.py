from __future__ import annotations
from typing import List, TypeVar
from data_structures.node import TreeNode
from data_structures.queues import Queue

T = TypeVar('T')


def level_order_traversal(root: TreeNode[T]):
    if root is None:
        return None

    result: List[T] = []
    queue = Queue()
    queue.enqueue(root)

    while queue.is_empty() is not True:
        node = queue.dequeue().get_value()
        result.append(node.get_value())

        if node.has_left():
            queue.enqueue(node.get_left())

        if node.has_right():
            queue.enqueue(node.get_right())

    return result
