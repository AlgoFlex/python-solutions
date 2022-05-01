from __future__ import annotations
from typing import TypeVar, Union
from data_structures.node import Node

T = TypeVar('T')


class DoublyLinkedListNode(Node[T]):
    def __init__(self, value: T, next: Union[T, None] = None, prev: Union[T, None] = None) -> None:
        super().__init__(value)
        self._next = next
        self._prev = prev

    def get_next(self) -> Union[T, None]:
        return self._next

    def get_prev(self) -> Union[T, None]:
        return self._prev

    def set_next(self, next_node: DoublyLinkedListNode[T]) -> None:
        self._next = next_node

    def set_prev(self, prev_node: DoublyLinkedListNode[T]) -> None:
        self._prev = prev_node
