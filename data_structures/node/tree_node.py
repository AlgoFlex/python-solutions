from __future__ import annotations
from typing import TypeVar, Union
from data_structures.node import Node

T = TypeVar('T')


class TreeNode(Node[T]):
    def __init__(self, value: Union[T, None] = None) -> None:
        super().__init__(value)
        self._left: Union[TreeNode, None] = None
        self._right: Union[TreeNode, None] = None

    def get_left(self) -> Union[TreeNode, None]:
        return self._left

    def get_right(self) -> Union[TreeNode, None]:
        return self._right

    def set_left(self, value: Union[TreeNode[T], T, None] = None) -> None:
        if isinstance(value, Node):
            self._left = value
        else:
            self._left = TreeNode(value)

    def set_right(self, value: Union[TreeNode[T], T, None] = None) -> None:
        if isinstance(value, Node):
            self._right = value
        else:
            self._right = TreeNode(value)

    def has_left(self) -> bool:
        return self._left is not None

    def has_right(self) -> bool:
        return self._right is not None
