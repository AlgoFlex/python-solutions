from __future__ import annotations
from typing import Generic, TypeVar, Union
from data_structures.node import DoublyLinkedListNode

T = TypeVar('T')


class DoublyDeque(Generic[T]):
    def __init__(self, capacity: Union[int, None] = None) -> None:
        self._left: Union[DoublyLinkedListNode[T], None] = None
        self._right: Union[DoublyLinkedListNode[T], None] = None
        self._capacity = capacity

    def append(self, value: T) -> DoublyLinkedListNode[T]:
        """Add value to the right side of the doubly deque."""
        pass

    def append_left(self, value) -> DoublyLinkedListNode[T]:
        """Add value to the left side of the doubly deque."""
        pass

    def pop(self) -> DoublyLinkedListNode[T]:
        """
        Remove and return an element from the right side of the deque.
        If no elements are present, raises an IndexError.
        """
        pass

    def pop_left(self) -> DoublyLinkedListNode[T]:
        """
        Remove and return an element from the left side of the deque.
        If no elements are present, raises an IndexError.
        """
        pass

    def capacity(self) -> int:
        """Maximum capacity of a deque or None if unbounded."""
        pass
