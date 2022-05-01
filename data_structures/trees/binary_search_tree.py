from __future__ import annotations
from typing import Generic, TypeVar, Union

T = TypeVar('T')


class BinarySearchTree(Generic[T]):
    def __init__(self, value: Union[T, None] = None) -> None:
        self._value = value
        self._left = None
        self._right = None

    def get_value(self) -> T:
        return self._value

    def get_left(self) -> Union[BinarySearchTree[T], None]:
        return self._left

    def get_right(self) -> Union[BinarySearchTree[T], None]:
        return self._right

    def insert(self, value: T) -> None:
        if value < self._value:
            if self._left is None:
                self._left = BinarySearchTree(value)
            else:
                self._left.insert(value)
        else:
            if self._right is None:
                self._right = BinarySearchTree(value)
            else:
                self._right.insert(value)

    def find(self, value: T) -> Union[BinarySearchTree[T], None]:
        if value == self._value:
            return self
        elif value < self._value:
            if self._left is None:
                return None
            else:
                return self._left.find(value)
        else:
            if self._right is None:
                return None
            else:
                return self._right.find(value)

    def pre_order_traversal(self):
        if self._value is None:
            return

        print(f'Depth={self.depth}, Value={self.value}')
        self._left.dfs_traversal()
        self._right.dfs_traversal()
