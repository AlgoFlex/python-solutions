from __future__ import annotations
from typing import TypeVar, Union
from data_structures.node import Node

T = TypeVar('T')


class SinglyLinkedListNode(Node[T]):
    def __init__(self, value: Union[T, None] = None, next: Union[SinglyLinkedListNode[T], None] = None) -> None:
        super().__init__(value)
        self._next = next

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node
