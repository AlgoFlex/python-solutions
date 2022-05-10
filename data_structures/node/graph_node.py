from __future__ import annotations
from typing import Generic, List, TypeVar

T = TypeVar("T")


class GraphNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.__value = value
        self.__children: List[GraphNode] = []

    @property
    def value(self) -> T:
        return self.__value

    @property
    def children(self) -> List[GraphNode]:
        return self.__children

    def add_child(self, node: GraphNode) -> None:
        self.children.append(node)

    def remove_child(self, node: GraphNode) -> None:
        if node in self.children:
            self.children.remove(node)
