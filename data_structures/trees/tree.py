from __future__ import annotations
from typing import TypeVar, Generic, Union
from data_structures.trees import TreeNode

T = TypeVar('T')


class Tree(Generic[T]):
    def __init__(self, value: Union[T, None] = None):
        self._root = TreeNode(value)

    def get_root(self) -> TreeNode[T]:
        return self._root



